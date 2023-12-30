
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
        <h4><a href = "#engine">Neural Engine for Strength Analysis :brain:</a></h4>
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
