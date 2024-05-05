from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

@app.route('/questions', methods=['GET'])
def get_questions():
    # Replace with your actual SQL Server config
    config = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=TATO-LAPTOP\SQLEXPRESS;DATABASE=prueba;UID=sa;PWD=123456'
    conn = pyodbc.connect(config)
    cursor = conn.cursor()
    cursor.execute('SELECT Id FROM dbo.Users')
    questions = [row[0] for row in cursor.fetchall()]
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)