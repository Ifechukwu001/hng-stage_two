"""Flask API application"""
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, g


app = Flask(__name__)


def get_db_conn() -> sqlite3.Connection:
    """Gets the database connection

    Returns:
        :obj:'sqlite3.Connection': Connection to the database
    """
    conn = getattr(g, "_dbconn", None)
    if conn is None:
        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def teardown(exception):
    conn = getattr(g, "_dbconn", None)
    if conn is not None:
        conn.close


@app.route("/api", methods=["POST"])
def create_person():
    """Creates a new person resource"""
    if request.is_json:
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")
        phone = data.get("phone")
        email = data.get("email")

        if not isinstance(name, (str, type(None))) \
           or not isinstance(age, (str, type(None))) \
           or not isinstance(phone, (str, type(None))) \
           or not isinstance(email, (str, type(None))):
            return jsonify({"status": "typeerror",
                            "message": "The data fields must be strings"
                            }), 400

        if name:
            created_at = datetime.isoformat(datetime.utcnow()).split(".")[0]
            conn = get_db_conn()
            cur = conn.execute("INSERT INTO persons (name, age, phone, email,"
                               " created_at) VALUES (?, ?, ?, ?, ?)",
                               (name, age, phone, email, created_at))
            conn.commit()

            return jsonify({"status": "success",
                            "id": cur.lastrowid}), 201

        return jsonify({"status": "failed",
                        "message": "Name must be passed"}), 400

    return jsonify({"status": "failed",
                    "message": "Payload must be in JSON"}), 400


@app.route("/api/<int:user_id>")
def fetch_person(user_id):
    """Fetches a person resource"""
    conn = get_db_conn().cursor()
    person = conn.execute("SELECT * FROM persons"
                          " WHERE id = ?", (user_id,)).fetchone()
    if person:
        person_json = {
            "name": person["name"],
            "age": person["age"],
            "phone": person["phone"],
            "email": person["email"],
            "id": person["id"],
            "created_at": person["created_at"]
        }
        return jsonify(person_json)
    else:
        return jsonify({"message": "Resource not available"}), 410


@app.route("/api/<int:user_id>", methods=["PUT"])
def update_person(user_id):
    """Update a person detail"""
    if request.is_json:
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")
        phone = data.get("phone")
        email = data.get("email")

        if not isinstance(name, (str, type(None))) \
           or not isinstance(age, (str, type(None))) \
           or not isinstance(phone, (str, type(None))) \
           or not isinstance(email, (str, type(None))):
            return jsonify({"status": "typeerror",
                            "message": "The data fields must be strings"
                            }), 400

        if name or age or phone or email:
            conn = get_db_conn()

            if name:
                conn.execute("UPDATE persons SET name=? WHERE id=?",
                             (name, user_id))
            if age:
                conn.execute("UPDATE persons SET age=? WHERE id=?",
                             (age, user_id))
            if phone:
                conn.execute("UPDATE persons SET phone=? WHERE id=?",
                             (phone, user_id))
            if email:
                conn.execute("UPDATE persons SET email=? WHERE id=?",
                             (email, user_id))

            conn.commit()

            return jsonify({"status": "success"}), 202
        return jsonify({"status": "unchanged"}), 200

    return jsonify({"status": "failed",
                    "message": "Payload must be in JSON"}), 400


@app.route("/api/<int:user_id>", methods=["DELETE"])
def delete_person(user_id):
    """Deletes a person resource"""
    conn = get_db_conn()
    conn.execute("DELETE FROM persons WHERE id=?", (user_id,))
    conn.commit()

    return jsonify({"status": "success"})
