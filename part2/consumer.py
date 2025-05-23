from confluent_kafka import Consumer


if __name__ == "__main__":
    consumer_conf = {
       "bootstrap.servers": "localhost:9092",
       "group.id": "kafka",
       "auto.offset.reset": "earliest",

       "security.protocol": "SASL_SSL",
       "ssl.ca.location": "secrets/ca.crt",  # Сертификат центра сертификации
       "ssl.certificate.location": "kafka-1-creds/kafka-1.crt",  # Сертификат клиента Kafka
       "ssl.key.location": "kafka-1-creds/kafka-1.key",  # Приватный ключ для клиента Kafka

       "sasl.mechanism": "PLAIN",  # Используемый механизм SASL (PLAIN)
       "sasl.username": "alice",  # Имя пользователя для аутентификации
       "sasl.password": "alice-secret",
       }

    consumer = Consumer(consumer_conf)
    consumer.subscribe(["topic_1", "topic_2"])

    try:
        while True:
            message = consumer.poll(timeout=2.0)

            if message is None:
                continue
            if message.error():
                print(f"Ошибка: {message.error()}")
                continue

            key = message.key().decode("utf-8")
            value = message.value().decode("utf-8")
            print(f"Получено сообщение: {key=}, {value=}, offset={message.offset()}")
    finally:
        consumer.close()
