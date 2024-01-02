
<div align = "center" style = "display:flex; flex-direction:row;">
  <img src = "https://img.shields.io/github/license/ranveerchaudhary/Mercurial?style=for-the-badge">
  <img src = "https://img.shields.io/github/issues/ranveerchaudhary/Mercurial?style=for-the-badge">
  <img src = "https://img.shields.io/github/issues-pr/ranveerchaudhary/Mercurial?style=for-the-badge">
</div>

<divC>
  <br>
  <img src="https://capsule-render.vercel.app/api?type=venom&height=210&text=Cipher&fontSize=160&color=0:240e68,100:ccc1e7&stroke=000000&fontColor=ffffff"/>
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
The project kicked off in 2019 as a fun way to explore Python, driven by the motivation to tackle a prevalent issue many individuals were facing at the time. 

The widespread reliance on weak passwords, often a combination of easily guessable information such as pet names, birthdays, or nicknames, presented a glaring security vulnerability. Compounding the matter, users habitually employed these weak passwords across multiple services, as highlighted by the alarming statistics.
<ul>
  <li>Only 12% of people always use unique passwords. (<a href = "https://www.lastpass.com/resources/ebook/psychology-of-passwords-2022">LastPass</a>, 2022)</li>  
  <li>1 out of 5 individuals admit including their birth year in their password. (<a href = "https://www.security.org/resources/online-password-strategies/">security.org</a>, 2023)</li>
  <li>96% of the most common passwords can be cracked by hacking tools in less than one second. (<a href = "https://resources.digitalshadows.com/whitepapers-and-reports/account-takeover-in-2022">Digital Shadows</a>, 2022)</li>
</ul>

Cipher arose as a response to these challenges, initially crafted in Python with a Tkinter-based user interface that blended nostalgia with a modern touch, including a sleek dark mode :) The password generation relied on the random library, a Pseudo Random Number Generator (PRNG), providing a secure solution, though not as robust as current standards. 

###

Version 2 marked a significant evolution, introducing password analysis through a set of conditional statements and a vault, fortified with SHA-256<a href = "https://en.wikipedia.org/wiki/Secure_Hash_Algorithms"><sup>1</sup></a> bit hash and HMAC<a href = "https://en.wikipedia.org/wiki/HMAC"><sup>2</sup></a>. Notably, salting was added to enhance security. Subsequent versions led to the current Version 7, the pinnacle of Cipher, offering the most refined and secure features to date.

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

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

<p>
Choosing the right random number generator is vital, as seen in cases like the alleged NSA backdoored <a href = "https://en.wikipedia.org/wiki/Dual_EC_DRBG">dual elliptic curve</a>. Initial the <a href = "https://docs.python.org/3/library/random.html">random</a> library's Pseudo Random Number Generator (PRNG) was used, which worked on the Mersenne Twister algorithm. However, it's crucial to highlight that theoretically, the seemingly random numbers it generates can be predicted, posing a substantial security risk. Even the official documentation advises against using such methods in cryptography and secure applications.

>Warning The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module.

While an alternative like the '<a href = "https://docs.python.org/3/library/secrets.html">secrets</a>' module, a Cryptographically Secure Random Number Generator (CSRNG), exists, we have embraced an even more advanced solution. Fortunately, the brilliant minds at the Australian National University (ANU) leverage quantum mechanics to measure the quantum fluctuations of the vacuum, resulting in a <a href = "https://qrng.anu.edu.au/">QRNG</a> (Quantum Random Number Generation), accessible through an API. The intricacies of how QRNG operates are beyond the scope of this project, but in essence, it introduces an unparalleled level of randomness and security. Just to give some context about its potency,

>Even if two identical generators were placed in identical environments with identical initial conditions, the streams of numbers generated would remain entirely uncorrelated.

While the API offers a free tier, it is restricted to 100 requests per month, as per our last check. You can sign up for the API and get the secret key <a href = "https://quantumnumbers.anu.edu.au/">here</a>. Users has the flexibility to choose the type of password they desire. The options include **alphanumeric**, **special characters**, and **r̶e̶a̶d̶a̶b̶l̶e̶**. The "readable" option was introduced for easily understandable passwords, but rigorous testing revealed a pattern of weakness. Consequently, this option has been **disabled** in the latest build. Passwords ranging from 8 to 100 characters can be generated. Even though a length of around 30 characters would be considered highly secure we've generously added extra space for the cybersecurity enthusiasts ;)
</p>

https://github.com/ranveerchaudhary/Cipher/assets/64607338/7b5decc3-0e86-46cb-99e5-04bb2f3ac6ab

<br>

<h3 id = "engine">2. Neural Engine :brain:</h3>

![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

<p>Why use neural networks instead of simple conditional statements in categorizing password strength? The latter can misrepresent it, leading to potential security flaws. For instance, while "abcd12345" seems weak for conditional statements, "Abcd@1234" is strong. Cipher utilizes neural networks for accurate password strength analysis.

The neural network was trained on a custom dataset curated by Ranveer, categorized into three labels: weak, medium, and strong. The dataset encompasses passwords from various sources, including infamous leaked <a href = "https://en.wikipedia.org/wiki/RockYou#Data_breach" >RockYou passwords</a> and other leaked passwords found on the internet, these passwords were then scraped using <a href = "https://www.crummy.com/software/BeautifulSoup/" >BeautifulSoup</a>. Additionally, passwords generated using Cipher and the QRNG were included.

Curating the dataset posed a unique challenge during the scraping process, as passwords could contain commas. To mitigate potential issues with CSV (Comma-Separated Values), we transitioned to TSV (Tab-Separated Values) by switching the delimiter. This ensured that passwords with commas were preserved without disrupting the dataset.

>Even if you don't use a cipher, always include a comma in your password. It will break the CSV format if your password ever gets leaked.

The data was fed into a meticulously designed Keras neural network, trained extensively over hundereds of epochs with finely tuned hyperparameters to capture the intricate non-linear patterns associated with password strength. The result? A cutting-edge password analysis system that precisely evaluates the robustness of generated passwords, and if Cipher says it's strong, then it's really strong — even by military standards.</p>

<div align = "center">
  <img src = "https://github.com/ranveerchaudhary/Cipher/blob/main/readme-assets/weakpasscipher.png">
  <img src = "https://github.com/ranveerchaudhary/Cipher/blob/main/readme-assets/weakpasswebsite.png">
  <figcaption>Comparing a weak password between cipher & <a href = "https://www.passwordmonster.com/">Password Monster</a></figcaption>
</div>

<br>

<h3 id = "vault">3. The Vault 👀</h3>

>The vault eliminates the hassle of remembering different passwords used across various services, thereby addressing the final problem mentioned above.

<p>
Every version of Cipher featured a vault, allowing users to save and view passwords. However, due to Cipher version 7 being deployed on a browser, a proper encrypted database is not feasible. Instead, a file system is employed to store encrypted passwords along with their corresponding platforms. These files are secured with a key (Master PIN). If users wish to view the passwords again, they can upload the .cipher file and use the key (Master PIN) that was used to encrypt the file. Users can create a new .cipher file for each new password, or they can append new passwords to already existing .cipher files (Please ensure to use the same Master PIN when appending new passwords to avoid any potential bugs).
</p>

##

<br>

<h2 id = "endnode">The End Note 🔚</h2>

<p>
Well, that's a wrap – that's all there is to know about Cipher. There are plenty of cool features that could be added in future versions, but, Ehh, I hate to break it to you; there won't be any future versions :,( There's a laundry list of improvements to be made, such as making Cipher responsive for different devices, adding a secure database, and implementing autofill credentials on various platforms, among other things. If you're as enthusiastic about Cipher or any tech that makes the world a better place as I am and want to contribute, you can find instructions in the <a href = "#contributions">contributions</a> section on how to add a stellar feature.

Reaching the current version took a considerable amount of time, perfecting every imperfection. While Cipher may have room for improvement, it is complete and stands as depicted. We've made efforts to future-proof Cipher, but inevitably, at some point, it might become ancient tech. However, my hope is that people will use it and appreciate it for what it is now. I understand Cipher might be overkill for Grandma's Facebook password, but sometimes, overengineering is the secret sauce behind great projects.
</p>

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
<ul>
<li>Email: <a href = "mailto:ranveerchaudhary1000@gmail.com">ranveerchaudhary1000@gmail.com</a></li>

<li>Portfolio Website: https://ranveerchaudhary.github.io</li>

<li>Linkedin Profile: https://www.linkedin.com/in/ranveerchaudhary1</li>
</ul>
