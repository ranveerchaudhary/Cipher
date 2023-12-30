
<div align = "center" style = "display:flex; flex-direction:row;">
  <img src = "https://img.shields.io/github/license/ranveerchaudhary/Mercurial?style=for-the-badge">
  <img src = "https://img.shields.io/github/issues/ranveerchaudhary/Mercurial?style=for-the-badge">
  <img src = "https://img.shields.io/github/issues-pr/ranveerchaudhary/Mercurial?style=for-the-badge">
</div>

<divC>
  <br>
  <img src="https://capsule-render.vercel.app/api?type=venom&height=210&text=Cipher&fontSize=160&color=0:240e68,100:ccc1e7&stroke=ffffff&fontColor=ffffff"/>
</div>

<h3 align = "center" >Revolutionizing Password Security with Quantum Mechanics</h3>

<br>

# Contents

<div >
  <ul>
    <li>
    <h3><a href = "#introduction">Introduction 📄</a></h3>
    <ul>
      <li>
        <h4><a href = "#decipher">The Decipher *️⃣</a></h4>
      </li>
      <li>
        <h4><a href = "#history">History :thought_balloon:</a></h4>
      </li>
      <li>
        <h4><a href = "#ui">The User Interface :iphone:</a></h4>
      </li>
    </ul>
    </li>
    <li>
      <h3><a href = "#btc">Behind the Curtain 🎭</a></h3>
      <ul>
      <li>
        <h4><a href = "#generation">Generation Mechanics :mechanical_arm:</a></h4>
      </li>
      <li>
        <h4><a href = "#engine">Neural Engine :brain:</a></h4>
      </li>
      <li>
        <h4><a href = "#vault">The Vault 👀</a></h4>
      </li>
    </ul>
    </li>
    <li>
      <h3><a href = "#endnode">The End Note 🔚</a></h3>
    </li>
    <li>
      <h3><a href = "#contributions">Get Involved :anchor:</a></h3>
    </li>
    <li>
      <h3><a href = "#contact">Reach Out :mailbox_with_mail:<a/></h3>
    </li>
  </ul>
</div>

##

<br>

<h2 id = "introduction">Introduction 📄</h2>

<h3 id = "decipher">1. The Decipher *️⃣</h3>
<p><strong>Cipher</strong> is a cutting-edge password generator and vault, utilizing quantum mechanics to create truly random and robust passwords. Cipher also employs neural networks to analyze passwords and stores them with military-grade encryption for enhanced security.</p>

<br>

<h3 id = "history" >2. History :thought_balloon:</h3>
<p>
The project kicked off in 2019 as a fun way to explore Python, driven by the motivation to tackle a prevalent issue many individuals were facing at the time. The widespread reliance on weak passwords, often a combination of easily guessable information such as pet names, birthdays, or nicknames, presented a glaring security vulnerability. Compounding the matter, users habitually employed these weak passwords across multiple services, as highlighted by the alarming statistics.
<ul>
  <li>Only 12% of people always use unique passwords. (<a href = "https://www.lastpass.com/resources/ebook/psychology-of-passwords-2022">LastPass</a>, 2022)</li>  
  <li>1 out of 5 individuals admit including their birth year in their password. (<a href = "https://www.security.org/resources/online-password-strategies/">security.org</a>, 2023)</li>
  <li>96% of the most common passwords can be cracked by hacking tools in less than one second. (<a href = "https://resources.digitalshadows.com/whitepapers-and-reports/account-takeover-in-2022">Digital Shadows</a>, 2022)</li>
</ul>
In response to these challenges, Cipher emerged as a solution. The initial iteration, developed exclusively in Python, featured a user interface implemented using the Tkinter library. Despite the UI exuding a nostalgic Windows 95 aesthetic, Cipher defied Tkinter's constraints, achieving a modern appearance with the added flair of a dark mode ;). The password generation mechanism relied on the random library, a Pseudo Random Number Generator (PRNG), offering a level of security that, although less robust than today's standards, was acceptably secure.

###

Version 2 marked a significant evolution, introducing password analysis capabilities through a set of conditional statements. The vault, a new addition in this version, leveraged the hashlib library to implement the SHA-256 bit hash (Secure Hashing Algorithm) [<sup>1</sup>](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) and HMAC [<sup>2</sup>](https://en.wikipedia.org/wiki/HMAC). Notably, salting was implemented to fortify the system against password-hash dictionaries. Subsequent versions featured minor updates, culminating in the current Version 7, which represents the pinnacle of Cipher's capabilities, offering the most refined and secure features to date.
</p>

<div align = "center" style = "display:flex; flex-direction:row;">
  <img src = "https://github.com/ranveerchaudhary/Cipher/blob/main/readme-assets/cipherv7.png">
  <figcaption>Cipher Version - 7</figcaption>
</div>

<br>

<h3 id = "ui" >3. The User Interface :iphone:</h3>

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<p>
As previously mentioned, the initial versions of Cipher were constructed atop the Tkinter library, which did not meet modern UI/UX standards. However, the most recent Version 7 has undergone a transformation, adopting the neomorphism design style and harnessing the Puppertino framework to achieve crisp graphics. To introduce fluid and dynamic animations, we've incorporated the Anime.js framework, orchestrating intricate movements that enhance the overall user experience.

<ul>
  <li> <a href = "https://github.com/codedgar/Puppertino">Puppertino</a> </li>
  <li> <a href = "https://animejs.com/">Anime.js</a> </li>
</ul>
    
Version 7 represents a substantial leap forward, surpassing its predecessors not only in terms of features but also in the realm of UI design. The layout has been meticulously architected, adhering to user experience guidelines to ensure seamless navigation. Both the vault and the save password sections have undergone a comprehensive revamp, aligning with the upgraded design principles to provide users with a visually appealing and user-friendly interface.
</p>


##

<br>

<h2 id = "btc">Behind the Curtain 🎭</h2>

<h3 id = "generation">1. Generation Mechanics :mechanical_arm:</h3>

<p>
The initial versions of Cipher relied on the <a href = "https://docs.python.org/3/library/random.html">random</a> library, which utilizes a Pseudo Random Number Generator (PRNG), specifically employing the Mersenne Twister algorithm. However, it's crucial to highlight that theoretically, the seemingly random numbers it generates can be predicted, posing a substantial security flaw, particularly in the realm of cybersecurity. Even the official documentation explicitly advises against using such methods in cryptography and other secure applications. 

>Warning The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module.

While an alternative like the '<a href = "https://docs.python.org/3/library/secrets.html">secrets</a>' module, a Cryptographically Secure Random Number Generator (CSRNG), exists, we have embraced an even more advanced solution. Fortunately, the brilliant minds at the Australian National University (ANU) leverage quantum mechanics to measure the quantum fluctuations of the vacuum, resulting in a <a href = "https://qrng.anu.edu.au/">QRNG</a> (Quantum Random Number Generation), accessible through an API.

The intricacies of how QRNG operates are beyond the scope of this project, but in essence, it introduces an unparalleled level of randomness and security. Just to give some context about its potency,

>Even if two identical generators were placed in identical environments with identical initial conditions, the streams of numbers generated would remain entirely uncorrelated.

Cipher harnesses this cutting-edge technology to generate truly random and robust passwords. The generation mechanics handle all the heavy lifting, ensuring the creation of resilient passwords that defy predictability.
</p>

<br>

<h3 id = "engine">2. Neural Engine :brain:</h3>

<p>The capabilities of neural networks have been harnessed to analyze password strength within Cipher. While earlier versions included this feature, they relied on simple if-else statements to categorize passwords based on their strength. Although seemingly functional, this approach can, in many cases, misrepresent password strength, introducing a potential security flaw.

To address this limitation, a neural network has been integrated into Cipher's latest version. The neural network is trained on a custom dataset curated by Ranveer, categorized into three labels: weak, medium, and strong. The dataset encompasses passwords from various sources, including infamous leaked <a href = "https://en.wikipedia.org/wiki/RockYou#Data_breach" >RockYou passwords</a> and other leaked passwords found on the internet, these passwords were then scraped using <a href = "https://www.crummy.com/software/BeautifulSoup/" >BeautifulSoup</a>. Additionally, passwords generated using Cipher and the QRNG were included.

Curating the dataset posed a unique challenge during the scraping process, as passwords, when used in the generation process, could contain commas. To mitigate potential issues with CSV (Comma-Separated Values), we transitioned to TSV (Tab-Separated Values) by switching the delimiter. This ensured that passwords with commas were preserved without disrupting the dataset.

>Even if you don't use a cipher, always include a comma in your password. It will break the CSV format if your password ever gets leaked.

The processed data was then input into a meticulously designed neural network implemented using Keras. The resulting model underwent extensive training over hundreds of epochs, with hyperparameters finely tuned to capture the intricate non-linear patterns associated with password strength.</p>

##

<br>

<h2 id = "contributions">Get Involved ⚓</h2>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##

<br>

<h2 id = "contact">Reach Out 📬</h2>

Email: ranveerchaudhary1000@gmail.com

Portfolio Website: [https://ranveerchaudhary.github.io](https://ranveerchaudhary.github.io)

Linkedin Profile: [https://www.linkedin.com/in/ranveerchaudhary1](https://www.linkedin.com/in/ranveerchaudhary1)
