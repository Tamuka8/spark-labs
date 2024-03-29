<link rel='stylesheet' href='../assets/css/main.css'/>

[<< back to main index](../README.md)

Lab 3.2 : Operations On Multiple RDDs
=====================================
### Overview
learn operations that work with multiple RDDs

### Depends On
None

### Run time
15 mins

### RDD Documentation :
http://spark.apache.org/docs/latest/


--------
Meetup Recommendation
--------
User1 attends meetups  m1, m2 and m3.  
User2 attends meetups  m2, m3, m4  and m5

<img src="../assets/images/3.2.png" style="border: 5px solid grey; max-width:100%;"/>

**Find meetups common to both users**

**Find meetups attened by either user1 or user2**  
**Note there are duplicates in result.  How will you remove dupes?**

**Find meetups that only user1 attends**

**Recommending meetups to user**   
user1 and user2 has a couple of meetups in common.  Let's use to this to recommend meetups to both users  
* meetups recommended for user1 : m4 & m5
* meetups recommended for user2 : m1


-----
Hints
-----

### Step 1: start spark shell

```
    $   ~/apps/spark/bin/spark-shell
```

### Step 2: create data sets using parallelize() method
```scala
    val u1 = sc.parallelize(List("m1", "m2", "m3"))
    val u2 = sc.parallelize(???)
```



### Step 3 : try the following operations in RDDs
`union`, `intersection`,  `distinct`,  `subtract`

```scala
// example
u1.union(u2).collect
```
