# Rpi-IOT-PLWHA-Assitance-hub
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">DIY et Objets connectés</h3>

  <p align="center">
 We will be waiting for the bribery bonus ;)
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Electrical diagrams</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Ce projet consiste en la création d'un hub IoT à part entière pour les personnes vivant avec le VIH/SIDA, il va les aider dans leurs tâches quotidiennes et faciliter leur vie. Les patients infectés par le VIH nouvellement diagnostiqués peuvent avoir peu de connaissances ou une image déformée. de la maladie du VIH. Une croyance répandue, en particulier à l'époque pré-HAART, est qu'il faudrait abandonner tout plan pour l'avenir et vivre en mauvaise santé pour le reste des jours à venir. Une forte conviction que l'infection par le VIH est mortelle et terminale peut entraîner la perte d'espoir dans la vie et la vie.

Et cet appareil connecté au cloud agira comme un assistant pour ces personnes qui ont un besoin urgent d'assistance et de soutien.


Tout d'abord, nous avons les combinaisons de capteurs à domicile, pour assurer le maximum de confort et les meilleures conditions de vie pour les patients sensibles, il se compose de :
-Capteur de température
-Capteur d'humidité
-Capteur de qualité de l'air
-Détecteur d'incendie
-Détecteur d'ouverture de fenêtre et de porte

Nous pouvons également ajouter l'automatisation pour la ventilation, la climatisation, les humidificateurs et les thermostats intelligents.

L'une de nos principales caractéristiques est la proposition de bilans de santé, de rappels, de mise en relation avec un médecin personnel et d'assistance psychologique.

Nous avons également créé une interface utilisateur entièrement personnalisée avec plus des fonctionnalités mentionnées présentées, mais en raison du manque de temps, nous ne présentons que l'interface utilisateur, voici le lien :
https://www.figma.com/file/ItIu93NUFY5YTfyziBAXDx/Smart-home-dashboard-free-light?node-id=0%3A1&t=yBjsy75tXor3wVvA-1
il est également joint en pdf dans les fichiers principaux

Pour la visualisation, visitez ce lien :  [https://thingspeak.com/channels/1966402](https://thingspeak.com/channels/1966402)

### Composants requis pour le prototype physique
Tarte aux framboises
Capteur DHT11
Capteur BMP180
Fils de cavalier

Étape 1 : Configuration du compte Thingspeak

Pour créer votre chaîne sur Thingspeak, vous devez d'abord vous inscrire sur Thingspeak. Si vous avez déjà un compte sur Thingspeak, connectez-vous avec votre identifiant et votre mot de passe.

Étape 2 : Créer un canal pour vos données

Une fois connecté, créez une nouvelle chaîne en cliquant sur le bouton « Nouvelle chaîne »
Configuration de Thingspeak pour la station météo Pi

Après avoir cliqué sur "Nouveau canal", entrez le nom et la description des données que vous souhaitez télécharger sur ce canal.

Entrez le nom de vos données, « Humidité » dans le champ 1, « Température » ​​dans le champ 2 et « Pression » dans le champ 3. Si vous souhaitez utiliser plus de champs, vous pouvez cocher la case à côté de l'option Champ et entrer le nom et la description de vos données.

Après cela, cliquez sur le bouton Enregistrer la chaîne pour enregistrer vos informations.

Étape 3 : clé API

Pour envoyer des données à Thingspeak, nous avons besoin d'une clé API unique, que nous utiliserons plus tard dans notre code pour télécharger nos données de capteur sur le site Web Thingspeak.
Cliquez sur le bouton "Clés API" pour obtenir votre clé API unique pour télécharger les données de votre capteur.
Clé API de ThingSpeak pour la station météo Raspberry Pi
Copiez maintenant votre "clé API" car nous devons l'utiliser dans notre code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Construit avec

Cette section doit répertorier tous les principaux frameworks/bibliothèques utilisés pour démarrer ce projet.

* Python
* ThingSpeak
* https://www.mathworks.com/help/thingspeak/writedata.html
* Figma
* AdafruitDHT

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Commencer

tout ce que vous avez à faire est d'exécuter le script python nommé final.py

### Conditions préalables
Avoir les bibliothèques nécessaires installées


import thingspeak
import time
import Adafruit_DHT
import requests


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Vous pouvez utiliser ce projet pour vos applications IOT et en tirer parti

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Electrical diagrams

<a href="https://imgbb.com/"><img src="https://i.ibb.co/5MqSPC4/rasp-dht11-bb-min.jpg" alt="rasp-dht11-bb-min" border="0"></a>

<img align="center"><a href="https://ibb.co/3z5v6Nv"><img src="https://i.ibb.co/HdLCwzC/317247122-471125848427931-3892022894364168050-n.jpg" alt="317247122-471125848427931-3892022894364168050-n" border="0"></a><br /><a target='_blank' href='https://geojsonlint.com/'></a><br /><img/>

Découvrez notre vidéo de démonstration sur Youtube :  https://www.youtube.com/watch?v=U4EdzMZB858

<p align="right">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Demo]:https://ibb.co/3z5v6Nv
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 