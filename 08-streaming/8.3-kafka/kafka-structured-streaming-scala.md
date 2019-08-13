<link rel='stylesheet' href='../../assets/css/main.css'/>

[<< back to main index](../../README.md)  /  

Lab 8.3b: Kafka Streaming
=================

### Overview
Setting up Kafka

### Depends On
[Kafka setup](1-kafka-setup.md)

### Run time
1hr - 1.5 hrs


## STEP 1: Get Kafka running
Follow [Kafka Streaming guide](1-kafka-setup.md) and have kafka running.

## STEP 2: Edit source file
Go to the project root directory
```bash
    $    cd ~/spark-labs/08-streaming/8.3-kafka
```

**=> Edit the file : `src/main/scala/x/KafkaStructuredStreaming.scala`**  
**There are no TODO items to fix at this point**

## STEP 3: Build the project
We will use `sbt` to build the project.  

** ==> Inspect the `build.sbt` file**
```bash
    $   cd ~/spark-labs/08-streaming/8.3-kafka

    #  compile
    $   sbt clean compile

    # Create an assembly (fat jar) using
    $   sbt package
```

**=> Inspect generated jar files**
```bash
    $ ls -l   target/scala-2.11/
```

**=> Notice the size difference in both jars.  What accounts for the 'fat jar's size?**   



## STEP 4: Running Kafka streaming
Make sure you have Kafka up and running.  For reference
* Terminal #1  : zookeeper
* Terminal #2  : Kafka broker
* Terminal #3  : Kafka console producer (we will paste data here)
* Terminal #4  : Ran Kafka consumer

Here is the screen shot (click on image to see full size image)

<a href="../../assets/images/8.3a-streaming-small.png"><img src="../../assets/images/8.3a-streaming-small.png" style="border: 5px solid grey; max-width:100%;"/></a>



**=> Launch kafka streaming application as follows**  
```bash
  $    ~/spark/bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0      --master local[2]   --driver-class-path logging/        --class x.KafkaStructuredStreaming  target/scala-2.11/kafka-streaming_2.11-1.0.jar  'clickstream'
```

Parameters explained:
* **localhost:9092**   - kafka broker
* **clickstream** - topic

## STEP 5: Feed some data into producer window (Terminal #3)
**=> Try typing / pasting the following text in terminal #3**  
```
foo
bar
baz
```

**=> Notice the kafka streaming console**  
```console

root
 |-- key: binary (nullable = true)
 |-- value: binary (nullable = true)
 |-- topic: string (nullable = true)
 |-- partition: integer (nullable = true)
 |-- offset: long (nullable = true)

-------------------------------------------
Batch: 1
-------------------------------------------
+----+-----+-----------+---------+------+--------------------+-------------+
| key|value|      topic|partition|offset|           timestamp|timestampType|
+----+-----+-----------+---------+------+--------------------+-------------+
|null| [61]|clickstream|        0|    10|2018-03-28 17:30:...|            0|
+----+-----+-----------+---------+------+--------------------+-------------+

```

Notice how the value is treated as binary

## STEP 6 : Change schema
- Edit the file : `src/main/scala/x/KafkaStructuredStreaming.scala`
- Choose 'option 2' where we specify schema for Kafka
- Save the file
- compile and run as follows

```bash
$ sbt clean package

$ ~/spark/bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0      --master local[2]   --driver-class-path logging/        --class x.KafkaStructuredStreaming  target/scala-2.11/kafka-streaming_2.11-1.0.jar  'clickstream'

```

Watch the output;  value shoudl be treated as string now.

```console
root
 |-- key: string (nullable = true)
 |-- value: string (nullable = true)
 |-- topic: string (nullable = true)
 |-- partition: integer (nullable = true)
 |-- offset: long (nullable = true)

-------------------------------------------
Batch: 1
-------------------------------------------
+----+-----+-----------+---------+------+--------------------+-------------+
| key|value|      topic|partition|offset|           timestamp|timestampType|
+----+-----+-----------+---------+------+--------------------+-------------+
|null| foo |clickstream|        0|    10|2018-03-28 17:30:...|            0|
+----+-----+-----------+---------+------+--------------------+-------------+

```
