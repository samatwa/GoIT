# goit-de-hw-06

## Concurrent sensor-data generation

Two producer instances generate readings and send them to `building_sensors`.

![Concurrent producers](./ScreenShots/producers.png)

## Filtered-topic output

Filtered records are sent to their corresponding Kafka topics.

![Output topics](./ScreenShots/kafka_topic_out.png)
