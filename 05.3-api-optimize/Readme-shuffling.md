

Lab 6.1 Managing Shuffles and avoiding unnecessary ones
=========================================================

### Overview
Managing and avoiding shuffles
 Here we will be loading sample datasets of netflix and will be understanding the following,
 
 1. How to avoid unnecessary shuffling
 2. How it is useful when shuffling is done
=========================================
**IMPORTANT**
Clear unwanted column rows in csv in both the input files.
It affects join results.
=========================================
### Depends On
 Should contain more than one node in the cluster for wide shuffle to happen

### Run time
20-30 mins


## STEP 1: Edit source file

Go to the project root directory

```bash
    $    cd <lab-folder>
```


**=> Edit file : `src/main/java/spark/basic/Shuffling.java`**  
**=> And fix the TODO items**



## STEP 2: Compile the project

We will use `maven` to build the project.  

**=> Inspect the `pom.xml` file**

The file will look follows:

``````
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.elephantscale</groupId>
  <artifactId>spark.basic</artifactId>
  <version>2.11</version>
   <properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<maven.compiler.source>1.8</maven.compiler.source>
		<maven.compiler.target>1.8</maven.compiler.target>
	</properties>
  <dependencies>
		<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-core -->
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-core_2.11</artifactId>
			<version>2.3.2</version>
		</dependency>

		<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-sql -->
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-sql_2.11</artifactId>
			<version>2.3.2</version>
		</dependency>

	</dependencies>
	<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-assembly-plugin</artifactId>
				<version>2.4.1</version>
				<configuration>
					<!-- get all project dependencies -->
					<descriptorRefs>
						<descriptorRef>jar-with-dependencies</descriptorRef>
					</descriptorRefs>
				</configuration>
				<executions>
					<execution>
						<id>make-assembly</id>
						<!-- bind to the packaging phase -->
						<phase>package</phase>
						<goals>
							<goal>single</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
</project>
````````

**=> Kick off a build**  
(This will take a few minutes for the first time you run it)

```bash
    # be in the project root level directory
    $   cd   <lab-folder>

    $   mvn package

    # to do a clean rebuild use
    $  mvn clean package
```

Make sure there are no errors and there is output in `target` dir.

```bash
    $  ls -l   target/
```

You should see output like follows

````console
drwxrwxr-x 2 sujee staff      4096 Jan 23 19:08 archive-tmp
drwxrwxr-x 3 sujee staff      4096 Jan 23 19:09 classes
drwxrwxr-x 2 sujee staff      4096 Jan 23 19:08 maven-archiver
drwxrwxr-x 3 sujee staff      4096 Jan 23 19:08 maven-status
-rw-rw-r-- 1 sujee staff      5273 Jan 23 19:08 spark.basic-2.11.jar
-rw-rw-r-- 1 sujee staff 128676623 Jan 23 19:08 spark.basic-2.11-jar-with-dependencies.jar
drwxrwxr-x 2 sujee staff      4096 Jan 23 19:08 test-classes
````
`spark.basic-2.11-jar-with-dependencies.jar`  is our code compiled.


## STEP 3: Test Application in Local Master Mode

```bash
    $  cd  ~/spark-labs/06-api-java

    $   ~/spark/bin/spark-submit --class 'spark.basic.Shuffling' --master local[*]  target/spark.basic-2.11-jar-with-dependencies.jar
```

**==> Checkout the Shell UI (4040)**   

**==> Hit Enter key to terminate the program**

**==> Turn off the logs by sending logs by `2> logs` **   

```bash
    $   ~/spark/bin/spark-submit --class 'spark.basic.Shuffling' --master local[*]  target/spark.basic-2.11-jar-with-dependencies.jar  2> logs
```


Now let's submit the application to Spark server

## STEP 4: Start Spark Server

```bash
    $  ~/spark/sbin/start-all.sh
```

**=> Check the Spark Server UI at port 8080.**  
**=> Note the Spark master URL.**  

<img src="../assets/images/4.1b.png" style="border: 5px solid grey; max-width:100%;"/>


## STEP 5: Submit the application

Use the following command to submit the job

```bash
    $  cd  ~/spark-labs/06-api-java

    $   ~/spark/bin/spark-submit --class 'spark.basic.Shuffling' --master MASTER_URL  target/spark.basic-2.11-jar-with-dependencies.jar 2>logs
```

* MASTER URL : substitute your spark master url
* for files you can try `README.md`

**=> Watch the console output**

It may look like this

```console
###Movies and their user reviews
+--------------------+-------------+
|          Movie Name|Total Reviews|
+--------------------+-------------+
|10 Things I Hate ...|            6|
|                10.5|            2|
|        12 Angry Men|            2|
|          12 Monkeys|           10|
|13 Conversations ...|            4|
|      13 Going on 30|            8|
| 16 Years of Alcohol|            2|
|2001: A Space Ody...|            2|
|2010: The Year We...|            2|
|            21 Grams|            8|
|        24: Season 1|            2|
|           25th Hour|            4|
|             28 Days|            2|
|       28 Days Later|            2|
|3000 Miles to Gra...|            2|
|40 Days and 40 Ni...|            2|
|      50 First Dates|           16|
|                  54|            4|
|                 61*|            2|
|  70 Years of Popeye|            2|
+--------------------+-------------+
only showing top 20 rows

###Oscar won movies with its release year
+---------------------+------------+-------------+
|Movie Name(Oscar won)|Release Year|Total Reviews|
+---------------------+------------+-------------+
|              Amadeus|        1984|            6|
|   Driving Miss Daisy|        1989|            6|
|               Gandhi|        1982|            6|
|        Out of Africa|        1985|            4|
|              Platoon|        1986|            4|
|             Rain Man|        1988|           10|
|  Terms of Endearment|        1983|            8|
|     The Last Emperor|        1987|            6|
+---------------------+------------+-------------+


```
The lines starting with `###` are output from our program


## STEP 6:  Configuring logging

#### To quickly turn off the logging:
Redirect the logs as follows `  2> logs`.   
All logs will be sent to `logs` file.  
```bash
    $  ~/spark/bin/spark-submit --class 'spark.basic.Shuffling' --master MASTER_URL  target/spark.basic-2.11-jar-with-dependencies.jar 2>  logs
```

#### Using log4j config
Spark by default logs at INFO level.  While there is a lot of useful information there, it can be quite verbose.

We have a `logging/log4j.properties` file.  Inspect this file

```bash
    $    cat   logging/log4j.properties
```


The file has following contents

```
# Set everything to be logged to the console
log4j.rootCategory=WARN, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n

# Settings to quiet third party logs that are too verbose
log4j.logger.org.eclipse.jetty=WARN
log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper=INFO
log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter=INFO

## set log levels for our loggers
## everything under 'x' package
#log4j.logger.x=INFO
## specific file
#log4j.logger.spark.basic.Shuffling=DEBUG
```



We provide `--driver-class-path logging/`  to spark-submit to turn off logging

Here is an example

```bash
    $   ~/spark/bin/spark-submit --class 'spark.basic.Shuffling' --master local[*]  --driver-class-path logging/  target/spark.basic-2.11-jar-with-dependencies.jar   
```
