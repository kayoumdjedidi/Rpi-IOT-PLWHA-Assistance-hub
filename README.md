# Rpi-IOT-PLWHA-Assitance-hub
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

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

This project consists of the creation of a fully-fledged IoT Hub for people living with HIV/AIDS, it is going to assist them with their daily tasks and facilitate their lives, Newly diagnosed HIV-infected patients may have little knowledge or a distorted picture of HIV disease. A commonly held belief, especially in the pre-HAART era, is that one would have to give up any plan for the future and live in ill health for the rest of the days to come. A strong belief that HIV infection is fatal and terminal may result in the loss of hope in life and living.

And this cloud-connected device will act as an assistant to these people in dire need of assistance and support.

First, we have the home sensors suits, to assure the maximum comfort and best living conditions for sensitive patients, it consists of:
-Temperature sensor
-Humidity sensor
-Quality of air sensor
-Fire detector
-Window and door opening detector

Also, we can add Automation for ventilation, AC, Humidifiers, and smart thermostats.

One of our key features is the proposal of checkups, reminders, linking with a personal doctor, and psychological assistance.

We have also created a fully custom UI with more of the mentioned features showcased, but due to the lack of time, we are only presenting the UI, here is the link:
https://www.figma.com/file/ItIu93NUFY5YTfyziBAXDx/Smart-home-dashboard-free-light?node-id=0%3A1&t=yBjsy75tXor3wVvA-1
it is also attached as a pdf in the main files

For visualisation, visit this link: [https://thingspeak.com/channels/1966402](https://thingspeak.com/channels/1966402)

### Components Required for the physical prototype
Raspberry Pi
DHT11 Sensor
BMP180 Sensor
Jumper Wires

Step 1: Thingspeak Account Setup

For creating your channel on Thingspeak you first need to Sign up on Thingspeak. In case if you already have an account on Thingspeak, sign in using your id and password.

Step 2: Create a Channel for Your Data

Once you Sign in, create a new channel by clicking “New Channel” button
Thingspeak Setup for Pi Weather Station

After clicking on “New Channel”, enter the Name and Description of the data you want to upload on this channel.

Enter the name of your data, ‘Humidity’ in Field1, ‘Temp’ in Field2 and ‘Pressure’ in Field3. If you want to use more Fields you can check the box next to Field option and enter the name and description of your data.

After this click on save channel button to save your details.

Step 3: API Key

To send data to Thingspeak, we need a unique API key, which we will use later in our code to upload our sensor data to Thingspeak Website.
Click on “API Keys” button to get your unique API key for uploading your sensor data.
API Key of ThingSpeak for Raspberry Pi Weather Station
Now copy your “API Key”  because we need to use this in our code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

This section should list any major frameworks/libraries used to bootstrap this project.

* Python
* Thinkspeak
* https://www.mathworks.com/help/thingspeak/writedata.html
* Figma
* AdafruitDHT

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

all you need to do is run the python script named final.py

### Prerequisites
Have the necessary libraries installed

import thingspeak
import time
import Adafruit_DHT
import requests


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can use this project for your IOT applications and build upon it

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Electrical diagrams

<a href="https://imgbb.com/"><img src="https://i.ibb.co/5MqSPC4/rasp-dht11-bb-min.jpg" alt="rasp-dht11-bb-min" border="0"></a>

<img align="center"><a href="https://ibb.co/3z5v6Nv"><img src="https://i.ibb.co/HdLCwzC/317247122-471125848427931-3892022894364168050-n.jpg" alt="317247122-471125848427931-3892022894364168050-n" border="0"></a><br /><a target='_blank' href='https://geojsonlint.com/'></a><br /><img/>

Check out our Demo video on Youtube: https://www.youtube.com/watch?v=U4EdzMZB858

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
