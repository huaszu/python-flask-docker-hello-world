FROM python:3.10.5
ADD . /hello-world
WORKDIR /hello-world
RUN pip install -r requirements.txt