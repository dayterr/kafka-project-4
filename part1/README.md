# зайти в терминал контейнера kafka-0
команда:
`docker exec -it kafka-0 bash`

# создание топика balanced_topic
команда:
`kafka-topics.sh --bootstrap-server localhost:9092 --topic balanced_topic --create --partitions 8 --replication-factor 3`

вывод:

[<img src="pics/step1.png">](http://example.com/)


# проверим состояние партиций
команда:
`kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic mytopic`

вывод:



