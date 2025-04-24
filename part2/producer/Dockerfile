FROM python:3.11-slim

WORKDIR /opt/custom-app

COPY producer.py /opt/custom-app/

RUN apt-get update && \
pip install kafka confluent-kafka && \
mkdir /opt/custom-app/secrets

CMD [ "python", "/opt/custom-app/producer.py" ]