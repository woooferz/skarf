# Skarf

![Build](https://img.shields.io/github/workflow/status/woooferz/skarf/Docker/master)

Self-Hosted Linktree/beacons.ai with easy configuration.

Demo: https://me.wooferz.dev

## Screenshot
![Screenshot of Skarf](https://i.imgur.com/Gi0RCWr.png)

## Installation Guide

### With Docker

First you'll have to make a new directory, where skarf can store its data.
Then make a docker-compose.yml that looks like this
```yaml
version: '3.3'
services:
    app:
        container_name: skarf
        ports:
            - '8080:80' # To expose skarf onto the host machine (remove this if you are using a reverse proxy such as traefik)
        volumes:
            - './static:/app/static' # To store data in the [website]/static/ url
            - './config:/app/config' # To store the config.yml config
        image: 'ghcr.io/woooferz/skarf:master'
```
After running, 2 new directories should pop up `static/` and `config/` it is important to copy the `config/config.yml` into the `config/` directory and restarting the container so skarf can configure itself and if you want your own images, you need to put files into `static/` and it can be accessed from the config with under the `static/` url.

Now you can run `docker-compose up -d`

## How did the name skarf come to be
Its simple, its a card type app thing, card -> scarf and for some reason there is a thing already called that! so I replaced the c with a k to make skarf
