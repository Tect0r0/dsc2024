import mysql.connector
import re
import csv

# Función para reemplazar emojis por su representación Unicode
def replace_emojis(text):
    emoji_regex = re.compile("["
        u"\U0001F600-\U0001F64F"  # Emoticonos
        u"\U0001F300-\U0001F5FF"  # Símbolos & pictogramas
        u"\U0001F680-\U0001F6FF"  # Transporte & mapas
        u"\U0001F1E0-\U0001F1FF"  # Banderas (iOS)
                           "]+", flags=re.UNICODE)
    cleaned_text = emoji_regex.sub('', text)
    return cleaned_text

try:
    # Establecer la conexión con la base de datos MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='BalooMowgli48.',
        database='datathon'
    )

    if conexion.is_connected():
        print("La conexión a la base de datos fue exitosa.")

    cursor = conexion.cursor()

    # Crear la tabla Tweets si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tweets (
        id_tweet INT PRIMARY KEY,
        date DATE,
        time TIME,
        tweet TEXT,
        Class VARCHAR(50)
    );
    """)

    # Leer el archivo CSV con los datos de los tweets
    with open('HeyData.csv', 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar la primera línea (encabezado)

        for fila in reader:
            id_tweet, date, time, tweet, Class = fila

            # Limpiar los emojis y otros caracteres especiales del tweet
            tweet = replace_emojis(tweet)

            # Insertar el tweet en la base de datos
            cursor.execute("INSERT INTO Tweets (id_tweet, date, time, tweet, Class) VALUES (%s, %s, %s, %s, %s)", (id_tweet, date, time, tweet, Class))

    conexion.commit()

except mysql.connector.Error as err:
    print(f"Algo salió mal: {err}")

finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("La conexión a la base de datos se ha cerrado.")