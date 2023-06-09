# Django and AWS S3 buckets for files management

[Complete Guide](https://medium.com/dev-genius/how-to-configure-a-django-application-with-s3-buckets-for-file-storage-9cea315316a4)

This is the codebase to setup Django application to use s3 bucket for:<br>
* file upload
* media files
* static files

# Setup & running locally

Create a .env file by copying the .env.sample provided and run:
```
docker compose build && docker compose up
```
to start the container. As an alternative, run:
```
docker compose -f docker-compose.dev.yml up --build
```
to build and run the container using the dev yaml file.
Make sure to externalize the db instance to be used. It can be in another container.

## Run tests
Run descriptive tests in the container using:
```
docker exec -it -w /app <container_name> pytest -rP -vv
```

Access the docs on:

```
http://localhost:10060/api/v1/doc
```


## Running In a Virtual Env

Create a virtual environment using:
```
mkvirtualenv <env_name>
```

Ensure you have installed `virtualenv` on your system and install dev dependencies using
```
pip install -r requirements/dev.txt
```

Run migrations using:
```
python manage.py makemigrations

python manage.py migrate
```

Run the server using:
```
python manage.py runserver
```




![Screenshot](screenshot1.webp)

![Screenshot](screenshot2.webp)
