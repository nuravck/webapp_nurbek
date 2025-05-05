from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "host": "nurbek2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route("/api/data", methods=["GET"])
def get_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
      "SELECT id, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score "
      "FROM tbl_siroj_students;"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    keys = ["id","gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course","math_score","reading_score","writing_score"]
    return jsonify([dict(zip(keys,row)) for row in rows])

@app.route("/add", methods=["POST"])
def add_data():
    data = request.json
    params = (
        data.get("gender"),
        data.get("race"),
        data.get("education"),
        data.get("lunch"),
        data.get("prep"),
        data.get("math"),
        data.get("reading"),
        data.get("writing")
    )
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tbl_nurbek_students (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, reading_score, writing_score) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",
        params
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status":"ok"}), 201

@app.route("/delete", methods=["POST"])
def delete_data():
    data = request.json
    id_to_delete = data.get("id")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_nurbek_students WHERE id = %s;", (id_to_delete,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
