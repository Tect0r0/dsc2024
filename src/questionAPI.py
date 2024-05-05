from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import pyodbc

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

    # Connect to MySQL Server
    # conn = mysql.connector.connect(**config)

    # Connect to Microsoft SQL Server
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=TATO-LAPTOP\SQLEXPRESS;DATABASE=datathon;UID=sa;PWD=123456')

    cursor = conn.cursor()
    # cursor.execute('SELECT mensaje FROM tweets_interaccion')
    cursor.execute('SELECT mensaje FROM dbo.Tweets_Interaccion')
    questions = [row[0] for row in cursor.fetchall()]
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)