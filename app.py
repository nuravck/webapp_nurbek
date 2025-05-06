from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Database connection info
db_config = {
    "host": "nurbek2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres"
}

# Connect to PostgreSQL
def get_connection():
    return psycopg2.connect(**db_config)
@app.route("/student", methods=["GET"])
def get_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_nurbek_students;")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    return jsonify(data)

@app.route("/add", methods=["POST"])
def add_data():
    data = request.get_json()

    # Extract and validate fields
    required_fields = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_cour>
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO tbl_nurbek_students 
            (gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, math_score, rea>
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data["gender"], data["race_ethnicity"], data["parental_level_of_education"],
            data["lunch"], data["test_preparation_course"], data["math_score"],
            data["reading_score"], data["writing_score"]
        ))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": f"Student added successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete", methods=["POST"])
def delete_data():
    data = request.json
    id = data.get("id")

    if not id:
        return jsonify({"error": "ID is required."}), 400

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM tbl_nurbek_students WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": f"Deleted {id} successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
