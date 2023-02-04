<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">git-ascii</h3>

  <p align="center">
    Creating "ASCII Art" using the contributions heatmap
    <br />
    <br />
    <a href="https://github.com/tariapper/git-ascii/wiki">Read Docs</a>
    ·
    <a href="https://github.com/tariapper/git-ascii/issues">Report Bug</a>
    ·
    <a href="https://github.com/tariapper/git-ascii/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project uses python's datetime to calculate the date that each commit must be sent. It uses os to send git commands to the terminal and exploits git's ability to create commits to the past (and future) to create art.


Sample inputs are stored in the /inputs folder. Each non-whitespace character represents a filled-in block on the GitHub contributions page. Only the first 7 lines and 53 characters of each line are parsed.

<!--
### Built With

* []()
* []()
* []()
-->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* python
* git
<!--  ```sh
  npm install npm@latest -g
  ```-->

### Installation

1. Create a copy of this repository

<a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://docs.github.com/assets/images/help/repository/use-this-template-button.png" alt="Use this template">
  </a>
   
2. Clone the repo
   ```sh
   git clone https://github.com/[YOUR-USERNAME]/[YOUR-REPO-NAME].git
   ```

<!-- USAGE EXAMPLES -->
## Usage

Navigate to the local repo and run the following line in the terminal

    python3 main.py -i inputs/hello.txt

To remove the commits, delete the repository.

_For more examples, please refer to the [Documentation](https://github.com/tariapper/git-ascii/wiki)_



<!-- ROADMAP -->
## Roadmap
* ~~Improve ease of use (remove need to copy files from one repo to another)~~
* _WIP_ Make use of the contribution page's full color palette
* Decrease runtime (create git tree manually as opposed to using git commits)
* Create more sample inputs

See the [open issues](https://github.com/tariapper/git-ascii/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Tariq - tariapper@outlook.com

Project Link: [https://github.com/tariapper/git-ascii](https://github.com/tariapper/git-ascii)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [otheneildrew's README template](https://github.com/othneildrew/Best-README-Template)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tariapper/git-ascii.svg?style=for-the-badge
[contributors-url]: https://github.com/tariapper/git-ascii/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tariapper/git-ascii.svg?style=for-the-badge
[forks-url]: https://github.com/tariapper/git-ascii/network/members
[stars-shield]: https://img.shields.io/github/stars/tariapper/git-ascii.svg?style=for-the-badge
[stars-url]: https://github.com/tariapper/git-ascii/stargazers
[issues-shield]: https://img.shields.io/github/issues/tariapper/git-ascii.svg?style=for-the-badge
[issues-url]: https://github.com/tariapper/git-ascii/issues
[license-shield]: https://img.shields.io/github/license/tariapper/git-ascii.svg?style=for-the-badge
[license-url]: https://github.com/tariapper/git-ascii/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tariapper
