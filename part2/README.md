# создать топики
сначала перейти в папку /bin
команда:  
`cd /bin`

команда:

```
./kafka-topics --bootstrap-server localhost:9091 --topic topic_1 --create --partitions 1 --replication-factor 1
```
и
```
./kafka-topics --bootstrap-server localhost:9091 --topic topic_2 --create --partitions 1 --replication-factor 1
```