# Contact-book-using-python-and-postgreSQL

#### an CLI program to save contacts using python and postgreSQL.
(Including Firstname, Lastname, Email, Phonenumber)\
The Contact book based in authentication user, using python and Postgresql


.
To configure postgreSQL, Enter own databae indformation inside app.py:
```bash
Database.initialise(database="contactbook",
                        user=" ",
                        password=" ",
                        host=" ",
                        port="5432"
                        ) #create a database connection
```


#### Sign-up as a new User:
```bash
python app.py --signup
```

#### login as a User:
```bash
python app.py --login
```

```bash
[add] to add a new contact into database.
[view] to view full contact information using firstname or lastname
[view -a] to view all Contacts
[delete] to delete a contact using contact ID
[update] to Update an existing Contact
```
