FROM python:3
ENV PYTHONUNBUFFERED 0
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
