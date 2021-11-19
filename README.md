# Advanced-CRUD-App-using-python-and-postgreSQL

a CLI script to manage contact information using python and PostgreSQL.\
(Including Firstname, Lastname, Email, Phonenumber)\
The script is based on user authentication.


![demo](https://github.com/signorrayan/Advanced-CRUD-app-using-python-and-postgresql/blob/master/Demo/pic.png)



- #### Install requirements and clone repository and change directory:
```bash
$ git clone https://github.com/signorrayan/Advanced-CRUD-app-using-python-and-postgresql.git
$ sudo apt update && sudo apt install python3-pip python3-venv
$ cd Advanced-CRUD-app-using-python-and-postgresql/
```

- #### To configure PostgreSQL, Enter your database indformation inside app.py:
```bash
Database.initialise(database="contactbook",
                        user=" ",
                        password=" ",
                        host=" ",
                        port="5432"
                        ) #create a database connection
```



- #### create tables in `contactbook` DB and extension(to encrypt password) in DB:
```bash
CREATE TABLE users(
  u_id SERIAL PRIMARY KEY,
  user_name VARCHAR(50) UNIQUE NOT NULL,
  password TEXT NOT NULL
  );

CREATE TABLE contact(
  c_id SERIAL PRIMARY KEY,
  first_name VARCHAR(100) not null,
  last_name VARCHAR(100) not null,
  email VARCHAR(200),
  phone_number VARCHAR(11),
  u_id int references users(u_id) not null
  );

CREATE EXTENSION IF NOT EXISTS pgcrypto;
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
