# Base64 Sites

## What is this thing?

Have you ever wanted to encode a tiny website in base64 but needed the link to be shared in mobile or otherwise handled by devices that only know about well-formed URLs? Well, me too.

Try it out <a href="base64-sites">here</a>.

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
