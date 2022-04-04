FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /book_220329
COPY requirements.txt /book_220329/requirements.txt

RUN pip install -r requirements.txt

COPY . /book_220329

CMD python manage.py runserver 0.0.0.0:8013