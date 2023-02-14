# Use an official Python runtime as a parent image
FROM python:3.10

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBYFFERED=1

COPY requirements.txt /backend

RUN pip3 install --upgrade pip --no-cache-dir -r requirements.txt && python manage.py makemigrations && python manage.py migrate

#CMD python manage.py makemigration
#
#CMD python manage.py migrate

COPY . /backend

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000