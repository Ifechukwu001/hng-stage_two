Author: Ogidi Ifechukwu

---

### Installation

Clone the repository:
```bash
git clone https://github.com/Ifechukwu001/hng-stage_two.git
```

Setup the python enviroment and install the packages in the file `requirements.txt`.
```bash
$ pip install -r requirements.txt
```

Setup the database by running the python script `init_db.py`.
```bash
$ python3 init_db.py
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

### Endpoints

#### Create a Person

- **Description**: Adds a new person resource to the database.
- **HTTP Method**: POST
- **Route**: `/api`

- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "age": "25",
        "phone": "2349043454342",
        "email": "j_doe@gmail.com"
    }
    ```
    _Note_: Only the `name` field is mandatory.

- **Response Body**:
    - `Success` - Status Code: 201
        ```json
        {
            "status": "success",
            "id": 1
        }
        ```
    - `Failed` - Status Code: 400
        ```json
        {
            "status": "failed",
            "message": "Name must be passed"/"Payload must be in JSON"
        }
        ```

#### Fetch a Person

- **Description**: Gets a person resource from the database.
- **HTTP Method**: GET
- **Route**: `/api/<user_id>`

- **Response Body**:
    - `Success` - Status Code: 200
        ```json
        {
            "name": "John Doe",
            "age": 25,
            "phone": "2349043454342",
            "email": "j_doe@gmail.com",
            "id": 1,
            "created_at": "2023-09-12T10:20:36"
        }
        ```
    - `Failed` - Status Code: 410
        ```json
        {
            "message": "Resource not available"
        }
        ```

#### Modify a Person

- **Description**: Updates a field in person resource on the database.
- **HTTP Method**: PUT
- **Route**: `/api/<user_id>`

- **Request Body**:
    ```json
    {
        "name": "",
        "age": "",
        "phone": "",
        "email": ""
    }
    ```
    _Note_: All fields are optional

- **Response Body**:
    - `Success` - Status Code: 202
        ```json
        {
            "status": "success"
        }
        ```

    - `Unchanged` - Status Code: 200
        ```json
        {
            "status": "unchanged"
        }
        ```

    - `Failed` - Status Code: 400
        ```json
        {
            "status": "failed",
            "message": "Payload must be in JSON"
        }
        ```

#### Delete a Person

- **Description**: Deletes a person resource from the database.
- **HTTP Method**: DELETE
- **Route**: `/api/<user_id>`

- **Response Body**:
    ```json
    {
        "status": "success"
    }
    ```
