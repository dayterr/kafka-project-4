from confluent_kafka import Consumer




if __name__ == "__main__":
   consumer_conf = {
       "bootstrap.servers": "localhost:9093",
       "group.id": "kafka",
       "auto.offset.reset": "latest",


       "security.protocol": "SSL",
       "ssl.ca.location": "ca.crt",  # Сертификат центра сертификации
       "ssl.certificate.location": "kafka-1-creds/kafka-1.crt",  # Сертификат клиента Kafka
       "ssl.key.location": "kafka-1-creds/kafka-1.key",  # Приватный ключ для клиента Kafka

   }
   consumer = Consumer(consumer_conf)
   consumer.subscribe(["topic_1"])


   try:
       while True:
           message = consumer.poll(timeout=0)

           if message is None:
               #print("py")
               continue
           if message.error():
               print(f"Ошибка: {message.error()}")
               continue


           key = message.key().decode("utf-8")
           value = message.value().decode("utf-8")
           print(f"Получено сообщение: {key=}, {value=}, offset={message.offset()}")
   finally:
       consumer.close()