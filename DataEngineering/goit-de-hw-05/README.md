# goit-de-hw-05

## Three Kafka topics

![Created topics](ScreenShots/1_create_topics.png)

## Concurrent sensor producers

Two program instances generate sensor readings and send them to `building_sensors`.

![First producer](ScreenShots/2_sensor_produser_1.png)
![Second producer](ScreenShots/2_sensor_produser_2.png)

## Processing and routing

The processor receives readings, selects the required data and forwards it to the relevant topics.

![Data processor](ScreenShots/3_data_processor.png)

## Filtered output

![Alert consumer output](ScreenShots/4_alert_consumer.png)
