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

## Pending

- Base64 encoding of uploaded images for pure JSON input? (33% size penalty)
- Current script execution is just `python server.py`. Runner script should allow extra functionality (ie: database selection)
