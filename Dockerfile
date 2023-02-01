FROM python:3.11

WORKDIR /usr/src/eventmap


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install --no-install-recommends libpq-dev gcc build-essential && \
    rm -rf /var/lib/apt/lists/*


EXPOSE 8000

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN ["python", "manage.py", "migrate"]

COPY . .

ENTRYPOINT ["python", "manage.py", "runserver", "10000" ]