from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# -----------------------------
# Database connection function
# -----------------------------
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "root"),
        database=os.environ.get("DB_NAME", "visits_db")
    )

# -----------------------------
# Home route
# -----------------------------
@app.route("/")
def home():
    db = get_db_connection()
    cursor = db.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert a new visit
    cursor.execute("INSERT INTO visits () VALUES ()")
    db.commit()

    # Count total visits
    cursor.execute("SELECT COUNT(*) FROM visits")
    visits = cursor.fetchone()[0]

    cursor.close()
    db.close()

    # Render HTML template
    return render_template("index.html", visits=visits)

# -----------------------------
# App entry point
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

