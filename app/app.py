from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/")
def home():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("INSERT INTO visits () VALUES ()")
    db.commit()

    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]

    cursor.close()
    db.close()

    return f"🚀 Two-Tier DevOps App is Running! | Visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

