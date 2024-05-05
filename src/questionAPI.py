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


    # Get total Dudas
    cursor.execute("SELECT COUNT(*) FROM tweets_interaccion WHERE Class = 'Duda'")
    total_dudas = cursor.fetchone()[0]

    # Get total Quejas
    cursor.execute("SELECT COUNT(*) FROM tweets_interaccion WHERE Class = 'Queja'")
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

    cursor.execute('SELECT mensaje FROM tweets_interaccion')
    #cursor.execute('SELECT mensaje FROM dbo.Tweets_Interaccion')
    questions = [row[0] for row in cursor.fetchall()]



    result = {
        'total_dudas': total_dudas,
        'total_quejas': total_quejas,
        'trending_topics': trending_topics,
        'questions': questions,
    }

    return jsonify(result)




if __name__ == '__main__':
    app.run(debug=True)