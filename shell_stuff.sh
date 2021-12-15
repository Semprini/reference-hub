cd c:\Dev\Kafka\kafka_2.13-2.8.0\bin\windows
zookeeper-server-start.bat ..\..\config\zookeeper.properties
kafka-server-start.bat ..\..\config\server.properties

kafka-topics.bat –zookeeper localhost:2181 –topic common.reference.anzsic_class.subscribe –create –partitions 3 –replication-factor 1

kafka-console-producer.bat -broker-list localhost:9092 -topic common.reference.anzsic_class.subscribe
