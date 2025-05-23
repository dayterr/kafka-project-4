import time
import uuid

from confluent_kafka import Producer


if __name__ == '__main__':
    config = {
        'bootstrap.servers': 'localhost:9092,kafka-1:9092,kafka-2:9092',
        #'client.id': 'app-producer',
        'acks': 1,  # Required for at least once delivery
        'retries': 3,

       # Настройки безопасности SSL
       'security.protocol': 'SASL_SSL',
       'ssl.ca.location': 'ca.crt',  # Сертификат центра сертификации
       'ssl.certificate.location': 'kafka-1-creds/kafka-1.crt',  # Сертификат клиента Kafka
       'ssl.key.location': 'kafka-1-creds/kafka-1.key',  # Приватный ключ для клиента Kafka


       # Настройки SASL-аутентификации
       'sasl.mechanism': 'PLAIN',  # Используемый механизм SASL (PLAIN)
       'sasl.username': 'alice',  # Имя пользователя для аутентификации
       'sasl.password': 'alice-secret',  # Пароль пользователя для аутентификации
   }
  
    producer = Producer(config)

    while True:
        key = f'key-{uuid.uuid4()}'
        value = 'SASL/PLAIN'
        producer.produce(
           'topic_1',
            #key=key,
            value=value,
            )
        producer.flush()
        print(f'Отправлено сообщение: {key=}, {value=}')
        time.sleep(5)
