# Task api

## Run the app:

With docker execute the following:
```sh
docker compose up
```

This will create the API, the database and a postgres admin.

**API url:** `localhost:8000`

**Postgres Admin:** `localhost:5454`

### Run migrations:

Enter the docker container with `docker exec -it  api /bin/bash` and execute the commands bellow:
```sh
alembic revision --autogenerate -m "New Migration"
alembic upgrade head
```