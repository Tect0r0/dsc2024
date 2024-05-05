from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/questions', methods=['GET'])
def get_questions():
    # Replace with your actual MySQL Server config
    config = {
        'user': 'root',
        'password': 'BalooMowgli48.',
        'host': 'localhost',
        'port': 3306,
        'database': 'datathon',
        'raise_on_warnings': True
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT id_tweet FROM tweets')
    questions = [row[0] for row in cursor.fetchall()]
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)