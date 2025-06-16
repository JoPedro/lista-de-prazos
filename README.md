<!-- Improved compatibility of retornar ao topo link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

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

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JoPedro/lista-de-prazos">
    <img src="/README-content/calendar.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Lista de Prazos</h3>
  <p align="center">
    Lista de prazos por identificador ordenada por data de início.
    <br />
    <a href="https://github.com/JoPedro/lista-de-prazos/issues/new?labels=bug">Reportar Bug</a>
    &middot;
    <a href="https://github.com/JoPedro/lista-de-prazos/issues/new?labels=enhancement">Sugerir Funcionalidade</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre">Sobre</a>
      <ul>
        <li><a href="#tecnologias">Tecnologias</a></li>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## Sobre

[![Product Name Screen Shot][product-screenshot]](https://hub.docker.com/r/jopedrop/lista-de-prazos)

Um projeto simples em Django para organizar prazos em uma lista legível onde os prazos com a data de início mais antiga aparecem primeiro. Este projeto foi feito para outra pessoa usar, logo há algumas funcionalidades mais específicas do seu caso de uso, como a presença de dois prazos.

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

### Tecnologias

- [![Django][Django]][Django-url]
- [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

<!-- GETTING STARTED -->

## Primeiros Passos

Este projeto é melhor executado em um contêiner Docker através de sua imagem distribuída publicamente. Veja a [página da imagem][pkg-url] na aba de [pacotes][Packages-url] deste repositório para mais informações. A imagem também está disponível no [Docker Hub][Docker-hub-img-url].

### Pré-requisitos

Para execução do projeto, é necessária a instalação da Docker Engine. Isso pode ser feito através da instalação do aplicativo [Docker Desktop][Docker-url], que vem com a Docker Engine já instalada, mas há também a opção de [instalar a Docker Engine individualmente](https://docs.docker.com/engine/install/).

Antes de prosseguir, verifique sua instalação da Docker Engine através do comando:

```sh
docker -v
```

O comando acima deve retornar a versão da sua instalação.

### Instalação e Execução

A execução do contêiner necessita de uma série de configurações obrigatórias. Um arquivo de instruções [Docker Compose][docker-compose-url] está disponível no repositório para facilitar a execução adequada, você também pode criar na sua máquina local um arquivo `docker-compose.yml` e colar o seguinte código, substituindo os valores marcados desta forma `<valor>` com os seus valores:

```yml
services:
  web:
    # Docker Hub: jopedrop/lista-de-prazos:latest
    image: ghcr.io/jopedro/lista-de-prazos:latest
    container_name: lista-de-prazos
    restart: always # opcional: reiniciar a cada boot
    ports:
      - 8000:8000
    depends_on:
      db:
        condition: service_healthy
        restart: true
    environment:
      DEBUG: False # IMPORTANTE: Este valor deve ser sempre False
      DJANGO_SECRET_KEY: <sua chave secreta Django>
      DJANGO_ALLOWED_HOSTS: localhost
      DJANGO_CSRF_TRUSTED_ORIGINS: http://localhost:8000
      DATABASE_ENGINE: postgresql
      DATABASE_NAME: <nome do banco de dados>
      DATABASE_USERNAME: <nome do usuário do BD>
      DATABASE_PASSWORD: <senha do BD>
      DATABASE_HOST: db # IMPORTANTE: deve ser o mesmo nome do serviço do BD
      DATABASE_PORT: 5432

  db:
    image: postgres:17
    container_name: postgres_db
    ports:
      - 5432:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: <nome do usuário do BD>
      POSTGRES_DB: <nome do banco de dados>
      POSTGRES_PASSWORD: <senha do BD>
    healthcheck:
      test:
        [
          "CMD-SHELL",
          "pg_isready -U <nome do usuário do BD> -d <nome do banco de dados>",
        ]
      interval: 10s
      retries: 5
      start_period: 30s
      timeout: 10s
volumes:
  postgres_data:
```

Sua chave Django pode ser gerada utilizando a versão web do pacote [Djecrety][djecrety-url].

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

<!-- USAGE EXAMPLES -->

## Documentação

### Listar Prazos

![Tela inicial][product-screenshot]

Esta é a tela inicial, nela estão listados todos os prazos cadastrados, em ordem cronológica segundo a data de início, você pode adicionar um novo prazo clicando no botão "CADASTRAR NOVO PRAZO".

### Cadastrar Prazos

![Cadastrar novo prazo][cadastrar-novo-prazo-url]

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

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

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

### Top contributors:

<a href="https://github.com/JoPedro/lista-de-prazos/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=JoPedro/lista-de-prazos" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->

## License

Distribuído sob a licença MIT. Veja [LICENSE][license-url] para mais informações.

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - joaopedrosilvaqueiroz@gmail.com

Project Link: [https://github.com/JoPedro/lista-de-prazos](https://github.com/JoPedro/lista-de-prazos)

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#readme-top">retornar ao topo</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/JoPedro/lista-de-prazos.svg?style=for-the-badge
[contributors-url]: https://github.com/JoPedro/lista-de-prazos/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JoPedro/lista-de-prazos.svg?style=for-the-badge
[forks-url]: https://github.com/JoPedro/lista-de-prazos/network/members
[stars-shield]: https://img.shields.io/github/stars/JoPedro/lista-de-prazos.svg?style=for-the-badge
[stars-url]: https://github.com/JoPedro/lista-de-prazos/stargazers
[issues-shield]: https://img.shields.io/github/issues/JoPedro/lista-de-prazos.svg?style=for-the-badge
[issues-url]: https://github.com/JoPedro/lista-de-prazos/issues
[license-shield]: https://img.shields.io/github/license/JoPedro/lista-de-prazos.svg?style=for-the-badge
[license-url]: /LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/joao-pedro-queiroz
[product-screenshot]: /README-content/tela-inicial.png
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
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[Docker]: https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Docker-hub-img-url]: https://hub.docker.com/r/jopedrop/lista-de-prazos
[pkg-url]: https://github.com/JoPedro/lista-de-prazos/pkgs/container/lista-de-prazos
[Packages-url]: https://github.com/JoPedro?tab=packages&repo_name=lista-de-prazos
[docker-compose-url]: /README-content/docker-compose.yml
[docker-pull-docs]: https://docs.docker.com/reference/cli/docker/image/pull/
[djecrety-url]: https://djecrety.ir/
[cadastrar-novo-prazo-url]: /README-content/cadastrar-novo-prazo.png
