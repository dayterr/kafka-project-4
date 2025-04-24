# создать топики

сначала создадим конфиг следующего содержания:  
```
echo 'security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="admin" password="admin-secret";
# Path to the keystore (if client authentication is required)
ssl.keystore.location=/etc/kafka/secrets/kafka.kafka.keystore.pkcs12
ssl.keystore.password=your-password
ssl.key.password=your-password
# Path to the truststore
ssl.truststore.location=/etc/kafka/secrets/kafka.kafka.truststore.jks
ssl.truststore.password=your-password
ssl.endpoint.identification.algorithm=' >> prop.cfg
```

затем создадим сами топики.  
команда:

```
kafka-topics --bootstrap-server localhost:9092 --topic topic_1 --create --partitions 1 --replication-factor 1 --command-config prop.cfg
```
и
```
kafka-topics --bootstrap-server localhost:9092 --topic topic_2 --create --partitions 1 --replication-factor 1 --command-config prop.cfg
```

# назначим правила доступа
для продьюсера отправка в topic_1.  
команда:
```
kafka-acls --bootstrap-server localhost:9092 \
--add \
--allow-principal User:alice \
--operation write \
--operation create \
--topic topic_1 \
--command-config prop.cfg
```

для продьюсера отправка в topic_2. 
команда:
```
kafka-acls --bootstrap-server localhost:9092 \
--add \
--allow-principal User:alice \
--operation write \
--operation create \
--topic topic_2 \
--command-config prop.cfg
```

для консьюмера чтение из topic_1.  
команда:
```
kafka-acls --bootstrap-server localhost:9092 \
--add \
--allow-principal User:alice \
--operation read \
— operation describe \
--group kafka \
--topic topic_1 \
--command-config prop.cfg
```

останавливаем контейнеры при необходимости.  
команда:  
```
docker stop part2-consumer-1 part2-producer-1
```

запускаем снова.  
команда:
```
docker start part2-consumer-1 part2-producer-1
```

если продьюсер не старует, запустим из контейнера.  
команда:
```
docker exec -it part2-producer-1 bash
```
и
```
python3 producer.py
```

запустим консьюмер из контейнера.  
команда:
```
docker exec -it part2-consumer-1 bash
```
и
```
python3 consumer.py
```

увидим ошибку авторизации, наш консьюмер не может читать из topic_2.
```
Ошибка: KafkaError{code=TOPIC_AUTHORIZATION_FAILED,val=29,str="Fetch from broker 1 failed: Broker: Topic authorization failed"}
```

далее будут сообщения по типу:
```
Получено сообщение: key='key-8dd0ed46-f250-4437-81a8-26f4a5bb0375', value='SASL/PLAIN', offset=121
Получено сообщение: key='key-23e702c5-6d6d-4dc9-9edb-ec3c138dae45', value='SASL/PLAIN', offset=122
Получено сообщение: key='key-7ce057dd-f7db-456f-91db-45f33e4fcf4e', value='SASL/PLAIN', offset=123
```

это сообщения из topic_1, как и требуется.