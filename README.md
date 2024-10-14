<img src="https://res.cloudinary.com/dfqctp7bq/image/upload/v1649007894/15_fit1vh.png">

This is the repository for <a href="https://rx-36.life/post/data-communication-between-django-and-google-calendar-api/" target="_blank"><span class="link">this blog post<span></a>.

I've created a simple application for communicating data between Django and the Google calendar API.

## How to download this repo locally and running the application

This description assumes the use of docker and windows11.  
And I use pycharm for my IDE.


1. Enter following command from the command line.
```
git clone https://github.com/DevWoody856/django_calendar_api.git
```

2. After downloading the repo, create an `.env` file in the root of the project.

3. In the .env file you created, write the following.

```python
DEBUG_VALUE=TRUE

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db_book_220329
DB_PORT=5432

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

service_account_email=************************
credentials=*************************
calendarId=********************
```

As a reminder, DB_HOST is the service name of the database in docker-compose.yaml.  
In this docker configuration, it is `db_book_220329`.

For the items related to google Calendar, service_account_email, credentials, and calendarId, please get your own in the GCP admin.

In particular, "credentials" must specify the path of the credentials file. So, first, get the credential file from GCP.
(See the blog post on how to get)

Also, this time the secret key is written directly in `settings.py`.

4. From the project root, enter the following command.

```python
docker-compose up --build
```

5. If you success `docker-compose up -build`, you can see the message "starting development server at http://0.0.0.0:8013/".   
Once it is up and running, please **open another terminal** while docker running, enter the following command.
This is the command that enters the dokcer side and launches the command line.

```python
docker-compose exec backend sh
```

6. When you are ready to enter a command, type the following command.
```python
python manage.py makemigrations
```

7. Then, after that
```python
python manage.py migrate
```

8. Database set is finished.
Enter the following command and the application should start.
```python
python manage.py runserver
```

9. If  you get the following message, it is working.
```python
Starting development server at http://127.0.0.1:8000/
```

### The actual application is accessed at `http://127.0.0.1:8013/`. Please note it.