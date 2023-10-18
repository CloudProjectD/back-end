
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![Pull Request][pr-shield]][pr-url] [![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CloudProjectD/back-end">

  </a>

<h3 align="center">KHU Market</h3>

  <p align="center">
    <br />
    <a href="https://github.com/CloudProjectD/back-end"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CloudProjectD/back-end/blob/main/README_kor.md">한국어</a>
    ·
    <a href="https://github.com/CloudProjectD/back-end/blob/main/README.md">English</a>
    <br />
    <br />
    <a href="https://github.com/CloudProjectD/back-end/issues">Report Issues</a>
    ·
    <a href="https://github.com/CloudProjectD/back-end/pulls">Pull Requests</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#mag-about-the-project">About The Project</a>
      <ul>
        <li><a href="#card_file_box-built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#rocket-getting-started">Getting Started</a>
      <ul>
        <li><a href="#zap-prerequisites">Prerequisites</a></li>
        <li><a href="#pencil2-configuration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#globe_with_meridians-project-structure">Project Structure</a></li>
    <li><a href="#memo-rest-api">REST API</a></li>
    <li><a href="#fire-contributing">Contributing</a></li>
    <li><a href="#closed_lock_with_key-license">License</a></li>
    <li><a href="#speech_balloon-contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## :mag: About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### :card_file_box: Built With
#### :bulb: Language & Framework
[![python][python]][python-url] [![fastapi][fastapi]][fastapi-url]
#### :bulb: Infrastructure
[![aws][aws]][aws-url]
#### :bulb: Environment (CI/CD, Package tools...)
[![Github-actions][Github-actions]][Github-actions-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## :rocket: Getting Started

### :zap: Prerequisites
Download and install packages and associated dependencies via `pip install`
* python
  ```sh
  pip install -r requirements.txt
  source ./venv/bin/activate
  ```
#### If you want to use Docker, then run `docker compose up -d`(Also it needs to stop with `docker compose down`).
#### ** Also, you have to run `black ./` before making pull request.

### :pencil2: Configuration
Setting environment variables through `.env`
```env
# .env

SECRET_KEY=secret
DEBUG=True
MYSQL_HOST=mysql-db
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=1234
DB_NAME=fastapi
BUCKET_NAME=
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_SESSION_TOKEN=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALLBACK_URL=

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## :globe_with_meridians: Project Structure

```markdown
├── Dockerfile
├── LICENSE
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── main.cpython-310.pyc
│   │   └── main.cpython-311.pyc
│   ├── api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── __init__.cpython-311.pyc
│   │   ├── dependencies
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── database.cpython-310.pyc
│   │   │   │   └── database.cpython-311.pyc
│   │   │   └── database.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   ├── http_error.cpython-310.pyc
│   │   │   │   ├── http_error.cpython-311.pyc
│   │   │   │   ├── validation_error.cpython-310.pyc
│   │   │   │   └── validation_error.cpython-311.pyc
│   │   │   ├── http_error.py
│   │   │   └── validation_error.py
│   │   └── routes
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-310.pyc
│   │       │   ├── __init__.cpython-311.pyc
│   │       │   ├── api.cpython-310.pyc
│   │       │   ├── api.cpython-311.pyc
│   │       │   └── users.cpython-311.pyc
│   │       ├── api.py
│   │       └── users.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── config.cpython-311.pyc
│   │   │   └── logging.cpython-311.pyc
│   │   ├── config.py
│   │   └── logging.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── base.cpython-311.pyc
│   │   │   ├── base_class.cpython-311.pyc
│   │   │   └── session.cpython-311.pyc
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-311.pyc
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-311.pyc
│   │   │   │   └── users.cpython-311.pyc
│   │   │   ├── jwt.py
│   │   │   ├── token.py
│   │   │   └── users.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-311.pyc
│   │       │   └── users.cpython-311.pyc
│   │       └── users.py
│   ├── resources
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   └── strings.cpython-311.pyc
│   │   └── strings.py
│   └── services
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   ├── authentication.cpython-311.pyc
│       │   ├── jwt.cpython-311.pyc
│       │   └── security.cpython-311.pyc
│       ├── authentication.py
│       ├── jwt.py
│       └── security.py
├── docker-compose.yml
├── fastapi.sql
├── requirements.txt
├── scripts
│   ├── format
│   ├── lint
│   ├── test
│   └── test-cov-html
├── setup.cfg
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_api
    │   ├── __init__.py
    │   ├── test_errors
    │   │   ├── __init__.py
    │   │   ├── test_422_error.py
    │   │   └── test_error.py
    │   └── test_routes
    │       ├── __init__.py
    │       ├── test_articles.py
    │       ├── test_authentication.py
    │       ├── test_comments.py
    │       ├── test_login.py
    │       ├── test_profiles.py
    │       ├── test_registration.py
    │       ├── test_tags.py
    │       └── test_users.py
    ├── test_schemas
    │   ├── __init__.py
    │   └── test_rw_model.py
    ├── test_services
    │   ├── __init__.py
    │   └── test_jwt.py
    └── testing_helpers.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## :memo: REST API



<!-- CONTRIBUTING -->
## :fire: Contributing
Please refer to `CONTRIBUTION.txt` for Contribution.

For issues, new functions and requests to modify please follow the following procedure. 🥰

1. Fork the Project
2. Create a Issue when you have new feature or bug, just not Typo fix
3. Create your Feature Branch from dev Branch (`git checkout -b feature/Newfeature`)
4. Commit your Changes (`git commit -m 'feat: add new feature'`)
5. Push to the Branch (`git push origin feature/Newfeature`)
6. Open a Pull Request to dev branch with Issues

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## :closed_lock_with_key: License
Please refer to `LICENSE.txt` for LICENSE.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## :speech_balloon: Contact

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/Eeap"><img src="https://avatars.githubusercontent.com/u/42088290?v=4" width="100px;" alt=""/><br /><sub><b>Sumin Kim</b></sub></a></td>
      <td align="center"><a href="https://github.com/dusdjhyeon"><img src="https://avatars.githubusercontent.com/u/73868703?v=4" width="100px;" alt=""/><br /><sub><b>Dahyun Kang</b></sub></a></td>
      <td align="center"><a href="https://github.com/nahyun0121"><img src="https://avatars.githubusercontent.com/u/71493251?v=4" width="100px;" alt=""/><br /><sub><b>Nahyun Kim</b></sub></a></td>
    </tr>
  </tobdy>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CloudProjectD/back-end.svg?style=flat
[contributors-url]: https://github.com/CloudProjectD/back-end/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CloudProjectD/back-end.svg?style=flat
[forks-url]: https://github.com/CloudProjectD/back-end/network/members
[stars-shield]: https://img.shields.io/github/stars/CloudProjectD/back-end.svg?style=flat
[stars-url]: https://github.com/CloudProjectD/back-end/stargazers
[issues-shield]: https://img.shields.io/github/issues/CloudProjectD/back-end.svg?style=flat
[issues-url]: https://github.com/CloudProjectD/back-end/issues
[pr-url]: https://github.com/CloudProjectD/back-end/pulls
[pr-shield]: https://img.shields.io/github/issues-pr/CloudProjectD/back-end.svg?style=flat
[license-shield]: https://img.shields.io/github/license/CloudProjectD/back-end.svg?style=flat
[license-url]: https://github.com/CloudProjectD/back-end/blob/master/LICENSE.txt

[python]: https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white
[python-url]: https://www.python.org/
[aws]: https://img.shields.io/badge/AmazonAWS-232F3E?style=flat&logo=AmazonAWS&logoColor=white
[aws-url]: https://aws.amazon.com/
[fastapi]: https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=black
[fastapi-url]: https://www.oracle.com/kr/cloud/
[Github-actions]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white
[Github-actions-url]: https://github.com/features/actions

