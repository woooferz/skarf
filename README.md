# Skarf
## NOTE: 
builds will no longer be available on ghcr.io, all builds will be on [Docker Hub](https://hub.docker.com/repository/docker/wooferz/skarf/general)

![Build](https://img.shields.io/github/workflow/status/woooferz/skarf/Docker/master?style=for-the-badge)
![Read the Docs](https://img.shields.io/readthedocs/skarf-docs?style=for-the-badge)
![Discord](https://img.shields.io/discord/973532704740110386?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/woooferz/skarf?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/woooferz/skarf?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/woooferz/skarf?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/woooferz/skarf?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/woooferz/skarf?style=for-the-badge)

Self-Hosted Linktree/beacons.ai with easy configuration.

[Demo](https://skarfdemo.wooferz.dev/) /  [Docs](https://skarf-docs.readthedocs.io/en/latest/index.html) / [Support Discord](https://discord.gg/VnskbWb4Ft)

## Screenshot

![Screenshot of Skarf - 1](https://i.imgur.com/wOaRRhN.png)
![Screenshot of Skarf - 2](https://i.imgur.com/NJctg6E.png)

## Installation Guide

### With Docker

First you'll have to make a new directory, where skarf can store its data.
Then make a docker-compose.yml that looks like this

```yaml
version: "3.3"
services:
  app:
    container_name: skarf
    ports:
      - "8080:80" # To expose skarf onto the host machine (remove this if you are using a reverse proxy such as traefik)
    volumes:
      - "./static:/app/static" # To store data in the [website]/static/ url
      - "./config:/app/config" # To store the config.yml config
    image: "wooferz/skarf:master"
```

After running, 2 new directories should pop up `static/` and `config/` it is important to copy the `config/config.yml` into the `config/` directory and restarting the container so skarf can configure itself and if you want your own images, you need to put files into `static/` and it can be accessed from the config with under the `static/` url.

Now you can run `docker-compose up -d`

## How did the name skarf come to be

Its simple, its a card type app thing, card -> scarf and for some reason there is a thing already called that! so I replaced the c with a k to make skarf
