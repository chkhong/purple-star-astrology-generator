# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#upgrade pip to latest version
RUN pip3 install --upgrade pip

# install requirements
COPY ./requirements.txt /app/requirements.txt

RUN pip install -U -r /app/requirements.txt

# copy app files to "app" directory
COPY ./app /app

EXPOSE 80