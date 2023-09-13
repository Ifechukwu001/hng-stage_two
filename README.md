# HNG Stage Two Task
## RESTful API

This is a simple RESTful API that performs the basic CRUD operations - Create, Read, Update and Delete, on a Person resource.

---

### Class Diagram
![Alttext](/Class%20Diagram.png)

---

### SetUp

The API is written in Python using the Flask framework and sqlite3 as its database.

So first of all, you must setup the python enviroment and install the packages in the file `requirements.txt`.
```bash
$ pip install -r requirements.txt
```

To setup the database, run the python script `init_db.py`.
```bash
$ python3 init_py
```

---

### Execution

After setting up the enviroment, you run the development server using:
```bash
$ python3 -m flask --app api run
```

For production, use gunicorn instead:
```bash
$ gunicorn api:app
```

---

### Testing

The API is publicly accessible at ...

and its Postman tests can be found [here](https://elements.getpostman.com/redirect?entityId=18989194-5585868f-a3c1-4c9b-9d0d-8be6c1c93da4&entityType=collection)

---

© [Ifechukwu Ogidi](https://github.com/Ifechukwu001)
