import mysql.connector

try:
    # Establecer la conexión con la base de datos MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='BalooMowgli48.',
        database='datathon'
    )

    cursor = conexion.cursor()

    # Crear la tabla Tweets_Interaccion si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tweets_Interaccion (
            id_tweet INT,
            Class VARCHAR(50),
            fue_respondido BOOLEAN,
            fecha_comentario DATE,
            hora_comentario TIME,
            fecha_respuesta DATE,
            hora_respuesta TIME,
            mensaje TEXT,
            FOREIGN KEY (id_tweet) REFERENCES Tweets(id_tweet)
        );
    """)

    # Leer los tweets de la tabla principal
    cursor.execute("SELECT id_tweet, Class, date, time, tweet FROM Tweets")

    for id_tweet, Class, date, time, mensaje in cursor.fetchall():
        # Filtrar los tweets que son dudas o quejas
        if Class in ('Duda', 'Queja'):
            # Insertar los datos en la nueva tabla
            cursor.execute("""
            INSERT INTO Tweets_Interaccion (id_tweet, Class, fue_respondido, fecha_comentario, hora_comentario, mensaje)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (id_tweet, Class, False, date, time, mensaje))

    conexion.commit()

except mysql.connector.Error as err:
    print(f"Algo salió mal: {err}")

finally:
    if (conexion.is_connected()):
        cursor.close()
        conexion.close()