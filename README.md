# Advanced-CRUD-App-using-python-and-postgreSQL

A cli script to manage contact information using python and PostgreSQL.\
(including Firstname, Lastname, Email, Phonenumber)\
The script is based on user authentication.


![demo](https://github.com/signorrayan/Advanced-CRUD-app-using-python-and-postgresql/blob/master/Demo/pic.png)



- #### Install requirements and clone repository and change directory:
```bash
$ sudo apt update && sudo apt install python3-pip python3-venv
$ git clone https://github.com/signorrayan/Advanced-CRUD-app-using-python-and-postgresql.git
$ cd Advanced-CRUD-app-using-python-and-postgresql/
```

- #### create DB, tables in `contactbook` DB and extension(to encrypt password) in DB:

```bash
$ su - postgres
$ psql

postgres=$ CREATE DATABASE contactbook;

postgres=$ \c contactbook

contactbook=$ CREATE TABLE users(
  u_id SERIAL PRIMARY KEY,
  user_name VARCHAR(50) UNIQUE NOT NULL,
  password TEXT NOT NULL
  );

contactbook=$ CREATE TABLE contact(
  c_id SERIAL PRIMARY KEY,
  first_name VARCHAR(100) not null,
  last_name VARCHAR(100) not null,
  email VARCHAR(200),
  phone_number VARCHAR(11),
  u_id int references users(u_id) not null
  );

contactbook=$ CREATE EXTENSION IF NOT EXISTS pgcrypto;

contactbook=$ \q

```

- #### to configure PostgreSQL, enter your database indformation inside app.py:
```bash
Database.initialise(database="contactbook",
                        user=" ",
                        password=" ",
                        host=" ",
                        port="5432"
                        ) #create a database connection
```


- #### Create Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirement.txt
```

- #### Sign-up as a new user:
```bash
python bin/app.py --signup
```

- #### login as a user:
```bash
python bin/app.py --login
```

```bash
[add] to add a new contact into database.
[view] to view full contact information using firstname or lastname
[view -a] to view all Contacts
[delete] to delete a contact using contact ID
[update] to Update an existing Contact
```
