FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /web_django/



