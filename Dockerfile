FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

RUN python manage.py migrate

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
