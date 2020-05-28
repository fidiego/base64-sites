# Base64 Sites

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fidiego/base64-sites)

## What is this thing?

Have you ever wanted to encode a tiny website in base64 but needed the link to be shared in mobile or otherwise handled by devices that only know about well-formed URLs? Well, me too.

Try it out [here](//base64-sites.herokuapp.com).

## Other Info

- Built with python3 and [starlette](https://www.starlette.io/).
- HTML formatted with [tidy](http://www.html-tidy.org/).
- JS formatted with [prettier](https://prettier.io/).
- Python formatted with [Black](https://pypi.org/project/black/).

## Dev Setup

**Install Dependencies**

```
pipenv install --dev
```

**Make a `.env` file**

```
cp env.default .env
```

**Run with honcho**

```
pipenv run honcho -f Procfile.dev start
```

## TODO

- [ ] figure out css for `/render` endpoint. Get rid of the excess space so iframe fills space with no scroll on body or html.
- [ ] make a js only version that can be deployed on netlify
