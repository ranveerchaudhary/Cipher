import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import keras

model = None
tokenizer = None
max_sequence_length = None

def init():
    global model, tokenizer, max_sequence_length
    data = pd.read_csv("production.tsv", sep = '\t')
    model = keras.models.load_model("model.h5")

    tokenizer = Tokenizer(char_level=True)
    tokenizer.fit_on_texts(data['password'])
    max_sequence_length = max(len(password) for password in data['password'])

def analyze(password):
    password_sequence = tokenizer.texts_to_sequences([password])
    password_sequence = pad_sequences(password_sequence, maxlen=max_sequence_length)

    predictions = model.predict(password_sequence, verbose = 0)
    predicted_strength = predictions.argmax(axis=-1)[0]

    strength_labels = ['low', 'medium', 'high']
    predicted_strength_label = strength_labels[predicted_strength]

    return str(predicted_strength_label)
