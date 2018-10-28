FROM python:3.6

RUN apt-get update && apt-get install -yq --fix-missing \
    python3-setuptools \
    python3-pip \
    gettext \
&& apt-get clean

RUN pip3 install --upgrade pip setuptools virtualenv

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY ./ /radioco/

WORKDIR /radioco/backend/

CMD ["../docker/django/scripts/start.sh"]