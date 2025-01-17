# Django

```bash

django-admin startproject projectname
# create app in Project
python manage.py startapp flights


```


# SQl with sqlite3


## 0 - create file and first table
```bash
touch flights.sql

sqlite3 flights.sql
```


## 1 - Create sql table Command
```sql

CREATE TABLE flights(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
   );

```

## 2- show tables command
```bash

.tables

```

## 3- get data from database
```bash

SELECT * FROM flights;

```

## 4 - add data to table inside data base
```bash

INSERT INTO flights (origin,destination,duration) VALUES ("New Yourk","London",415);

```

## 5- additional 
```bash

.mode columns
.headers yes

SELECT * FROM flights;

```

## 6- Function -> select specific row (value) or have pattern 
```bash

# WHERE (condition of value we want)

SELECT * FROM flights WHERE origin ="New Yourk";

SELECT * FROM flights WHERE origin ="New Yourk" AND destination ="Paris";

SELECT * FROM flights WHERE origin In ("New Yourk","Lima");

SELECT * FROM flights WHERE origin LIKE "%a%"


# AVERAGE
# COUNT
# MAX
# MIN
# SUM
# ...

```

## UPDATE
```bash

UPDATE flights
  SET duration =430;
  WHERE origin ="New Yourk"
  And destination ="London"
  
```

## DELETE
```bash

DELETE FROM flights WHERE destination = "New Yourk";


```

## other Caluses

```bash
# LIMIT
# ORDER BY
# GROUP BY
# HAVING
#....

```


## Foreign Keys -> To Link Tables Together
### JOIN
```bash

SELECT first,origin,destination FROM flights JOIN passengers ON passengers.flight_id = flight_id

# --- JOINs

# JOIN / INNER JOIN 
# LEFT OUTER JOIN
# RIGHT OUTER JOIN
# FULL OUTER JOIN

```


## Create INDEX to make it more efficiency
```bash

Create INDEX name_index OV passengers (last);

```


## SQL Injection Attacks (we )
```bash
# [ "-- ]-> in sql mean ignore any thing come after it 
WHERE username = "hacker"--" AND password="";

# how to save us 
# use layer on sql orm or protect sql command

```

## Race Condtions 
### // two thing happen in same time
. like two user in social make like in same time 
#### some solve
. make lock in data base .. 

```bash



```
