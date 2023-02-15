FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000
