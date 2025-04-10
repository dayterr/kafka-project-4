# зайти в терминал контейнера kafka-0
команда:
`docker exec -it kafka-0 bash`

# создание топика balanced_topic
команда:
`kafka-topics.sh --bootstrap-server localhost:9092 --topic balanced_topic --create --partitions 8 --replication-factor 3`

вывод:

[<img src="pics/step1.png">](https://github.com/dayterr/kafka-project-4/blob/main/part1/pics/step1.png)

<!---
можно посмотреть картинку step1.png в директории pics
-->

# проверим состояние партиций
команда:
`kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic balanced_topic`

вывод:

[<img src="pics/step2.png">](https://github.com/dayterr/kafka-project-4/blob/main/part1/pics/step2.png)

<!---
можно посмотреть картинку step2.png в директории pics
-->