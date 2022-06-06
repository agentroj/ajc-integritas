FROM python:3.6.7

# Env
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /var/www/mycv2
WORKDIR /var/www/mycv2

COPY requirements.txt /var/www/mycv2/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /var/www/mycv2/
