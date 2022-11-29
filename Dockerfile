FROM python:3.11

WORKDIR /usr/src/eventmap

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install --no-install-recommends libpq-dev gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]