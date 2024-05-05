import mysql.connector
import pyodbc

try:
    # Establecer la conexión con la base de datos MySQL
    # conexion = mysql.connector.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     password='BalooMowgli48.',
    #     database='datathon'
    # )

    # Establecer la conexion con la base de datos Microsoft SQL Server
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=TATO-LAPTOP\SQLEXPRESS;DATABASE=datathon;UID=sa;PWD=123456')

    cursor = conexion.cursor()

    # Crear la tabla Tweets_Interaccion si no existe MySQL
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS Tweets_Interaccion (
    #         id_tweet INT,
    #         Class VARCHAR(50),
    #         fue_respondido BOOLEAN,
    #         fecha_comentario DATE,
    #         hora_comentario TIME,
    #         fecha_respuesta DATE,
    #         hora_respuesta TIME,
    #         mensaje TEXT,
    #         respuesta TEXT,
    #         FOREIGN KEY (id_tweet) REFERENCES Tweets(id_tweet)
    #     );
    # """)

    # Crear la tabla Tweets_Interaccion si no existe Microsoft SQL Server
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dbo.Tweets_Interaccion' AND xtype='U')
        BEGIN
            CREATE TABLE Tweets_Interaccion (
                id_tweet INT,
                Class VARCHAR(50),
                fue_respondido BIT,
                fecha_comentario DATE,
                hora_comentario TIME,
                fecha_respuesta DATE,
                hora_respuesta TIME,
                mensaje VARCHAR(MAX),
                respuesta VARCHAR(MAX),
                FOREIGN KEY (id_tweet) REFERENCES Tweets(id_tweet)
            );
        END
    """)

    # Leer los tweets de la tabla principal
    cursor.execute("SELECT id_tweet, Class, date, time, tweet FROM Tweets")

    for id_tweet, Class, date, time, mensaje, respuesta in cursor.fetchall():
        # Filtrar los tweets que son dudas o quejas
        if Class in ('Duda', 'Queja'):
            # Insertar los datos en la nueva tabla MySQL
            # cursor.execute("""
            # INSERT INTO Tweets_Interaccion (id_tweet, Class, fue_respondido, fecha_comentario, hora_comentario, mensaje, respuesta)
            # VALUES (%s, %s, %s, %s, %s, %s, %s)
            # """, (id_tweet, Class, False, date, time, mensaje, respuesta))

            # Insertar los datos en la nueva tabla Microsoft SQL Server
            cursor.execute("""
            INSERT INTO Tweets_Interaccion (id_tweet, Class, fue_respondido, fecha_comentario, hora_comentario, mensaje, respuesta)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (id_tweet, Class, False, date, time, mensaje, respuesta))

    conexion.commit()

# except mysql.connector.Error as err:
#     print(f"Algo salió mal: {err}")

except pyodbc.Error as err:
    print(f"Algo salió mal: {err}")

finally:
        cursor.close()
        conexion.close()