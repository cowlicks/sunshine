FROM python:3.5.2-slim

MAINTAINER Blake Griffith <blake.a.griffith@gmail.com>

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN apt-get -y install nginx supervisor
RUN pip install --no-cache-dir gunicorn Flask

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY sunshine /usr/src/app/sunshine

# nginx setup
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# supervisor setup
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/
COPY gunicorn.conf /etc/supervisor/conf.d/

EXPOSE 80
CMD ["/usr/bin/supervisord"]
