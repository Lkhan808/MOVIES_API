FROM python:3.10

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /dj_movies/

COPY ./req.txt /dj_movies/
RUN pip install -r /dj_movies/req.txt

COPY . /dj_movies/


