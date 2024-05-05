from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
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


    # Get total Dudas
    cursor.execute("SELECT COUNT(*) FROM tweets_interaccion WHERE Class = 'Duda' AND fue_respondido = 0")
    total_dudas = cursor.fetchone()[0]

    # Get total Quejas
    cursor.execute("SELECT COUNT(*) FROM tweets_interaccion WHERE Class = 'Queja' AND fue_respondido = 0")
    total_quejas = cursor.fetchone()[0]

    
    
    # Get trending topics
    topics = {
    'App': ['app', 'aplicacion'],
    'Cuenta': ['cuenta'],
    'Tarjetas': ['TDC', 'linea de credito'],
    # Add more topics as needed
    }
    trending_topics = []

    cursor.execute("SELECT COUNT(*) FROM tweets_interaccion")
    total_general = cursor.fetchone()[0]
    for topic, keywords in topics.items():
        count = 0
        for keyword in keywords:
            cursor.execute(f"SELECT COUNT(*) FROM tweets_interaccion WHERE LOWER(mensaje) LIKE '%{keyword.lower()}%'")
            keyword_count = cursor.fetchone()[0]
            count += keyword_count
            total_general -= keyword_count
        trending_topics.append({'topic': topic, 'count': count})

    trending_topics.append({'topic': 'General', 'count': total_general})

    cursor.execute('SELECT mensaje FROM tweets_interaccion WHERE fue_respondido = 0')
    questions = [row[0] for row in cursor.fetchall()]



    result = {
        'total_dudas': total_dudas,
        'total_quejas': total_quejas,
        'trending_topics': trending_topics,
        'questions': questions,
    }

    return jsonify(result)

@app.route('/answer', methods=['POST'])
def answer_question():
    # Get the question and answer from the request data
    data = request.get_json()
    question = data['question']
    answer = data['answer']

    now = datetime.now()

    fecha_respuesta = now.strftime("%Y-%m-%d")
    hora_respuesta = now.strftime("%H:%M:%S")

    # Connect to the database MySQL
    # conn = mysql.connector.connect(**config)

    # Connect to the database MSSQL
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=TATO-LAPTOP\SQLEXPRESS;DATABASE=datathon;UID=sa;PWD=123456')
    cursor = conn.cursor()

    # Update the database
    cursor.execute(f"UPDATE tweets_interaccion SET respuesta = '{answer}', fue_respondido = 1, fecha_respuesta = '{fecha_respuesta}', hora_respuesta = '{hora_respuesta}' WHERE mensaje = '{question}'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(debug=True)