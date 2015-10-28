Carmack
=======

`Carmack` is a CRUD app for a putative car collector (ironic because, although John Carmack collected Ferraris, he was more likely to be writing super low level `C` graphics).

The client-side (`HTML/CSS/JavaScript`) is completely static and divorced from the back-end (`Bottle/Peewee/Sqlite`). The back-end is currently meant to be run locally. They communicate exclusively via a REST api.

Testing via `requests` and `py.test` covers all functionality, simulating all HTTP scenarios.

## API

The API is inspired by [Parse.com](https://parse.com/docs/rest/guide)'s REST API defaults:

| URL | HTTP Verb | Functionality |
| --- | --------- | --------------|
| `/autos` | `GET` | Queries
| `/autos` | `POST` | Creating Objects
| `/autos/<auto_id:int>` | `GET` | Retrieving Objects
| `/autos/<auto_id:int>` | `PUT` | Updating Objects
| `/autos/<auto_id:int>` | `DELETE` | Deleting Objects

## Installation

`setup.py` script would be ideal, but such a barebones app isn't going on PyPI, so it doesn't benefit that much from that kind of configuration. It would perhaps end on Heroku one day, in which case this kind of script is more applicable.

1. Download source
2. Execute `pip install -r requirements.txt`
3. Run `python server.py`
4. Interact via HTTP directly, run tests, or access `localhost:8080` for a barebones demo

## Pending/Notes

- Base64 encoding of uploaded images for pure JSON input? (33% size penalty)
- Current script execution is just `python server.py`. Runner script should allow extra functionality (ie: database selection)
- Makefile used (abused?) to offer a very easy REPL test cycle in Sublime Text 3 without incurring a lot of overhead in terms of configuration files. May break on Windows.
