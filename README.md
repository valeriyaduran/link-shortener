## link-shortener
### Description:
Service for making long links shortened (similar to bitly.com)

### Service installation and launching:
Preconditions:
- Docker must be installed
- Docker daemon must be running
1) Clone the repository: git clone https://github.com/valeriyaduran/link-shortener.git
2) Launch the service: from the project working directory enter the following command in the terminal: 'docker compose up' or 'sudo docker compose up' (depending on your permissions)
3) Apply migrations: enter the following command in the terminal of 'link-shortener-fastapi' container: 'alembic upgrade head'

### Working with the service:

1) To get a shortened link send a POST request containing the origin_link.

**Request example**:
```
curl --location 'http://0.0.0.0:8080/shortened_link' \
--header 'Content-Type: application/json' \
--data '{"origin_link": "https://docs-python.ru/standart-library/modul-time-python/funktsija-process-time-modulja-time/"}'
```
**Response example**:
```
"http://shortener.tt/BUwGAZczgK"

------------------------
200 status code returned
```

2) To delete a shortened link and related long link send a DELETE request containing the link_id in the request url.

**Request example**:
```
curl --location --request DELETE 'http://0.0.0.0:8080/shortened_link/BUwGAZczgK' \
--data ''
```
**Response example**:
```
""
------------------------
204 status code returned
```
*Note: db credentials are stored in .env.dev (you can check .env.dev.example)*

### Testing:
Tests are stored in "tests" directory.    
Tests are implemented for link_shortener.py module.

#### Tests launching:
To run tests enter the following command in the terminal of 'link-shortener-fastapi' container:
```
export PYTHONPATH=. && pytest
```

#### Code style testing:
To check the code for stylistic errors and standards violations enter the following command from the project’s working directory in the terminal:
```
flake8 .
```

### Project tech stack:
- python 3.10.7
- fastapi
- postgres
- sqlalchemy
- alembic
- docker
- pytest
- flake8
- pipenv
  











