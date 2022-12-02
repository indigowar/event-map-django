# event-map-django

## Deploy

env file example:
```
// just application enviroment(local or prod)
APP_ENV=prod
// host where this application will works, need for django to accept requests
HOST=host
// database settings
POSTGRES_DB_HOST=db_host
POSTGRES_DB_NAME=db_name
POSTGRES_DB_PASSWORD=db_pasword
POSTGRES_DB_PORT=db_port
POSTGRES_DB_USER=db_user

```


## Filtration

Request:

If any of the fields are unused, you should exclude from request.

```json
{
"subjects": [
id1,
id2,
...
],
"competitors": [
id1,
id2,
...
],
"founding_range": {
"low": 0,
"high": 100
},
"co_founding_range": {
"low": 0,
"high": 15
},
"founding_type": [
id1,
id2,
id3
].
"submission_deadline": {
"start": "YYYY-MM-DD",
"end": "YYYY-MM-DD"
},
"trl": [
...
],
}
```
