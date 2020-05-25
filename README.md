# Base64 Sites

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fidiego/base64-sites)

## What is this thing?

Have you ever wanted to encode a tiny website in base64 but needed the link to be shared in mobile or otherwise handled by devices that only know about well-formed URLs? Well, me too.

Try it out <a href="//base64-sites.herokuapp.com">here</a>.

## Dev Setup

**Install Dependencies**

```
pipenv install
```

**Make a `.env` file with the following variables:**

```
HOST=127.0.0.1
PORT=8000
```

**Run with honcho**

```
pipenv run honcho -f Procfile.dev start
```

## TODO

- [ ] figure out css for `/render` endpoint. Get rid of the excess space so iframe fills space with no scroll on body or html.

## Other Info

- Built with python3 and <a href="https://www.starlette.io/">starlette</a>.
- HTML formatted with <a href="http://www.html-tidy.org/">tidy</a>.
- jJS formatted with <a href="https://prettier.io/">prettier</a>.
- Python formatted with <a href="https://pypi.org/project/black/">Black</a>.
