import mysql.connector
import os
from mysql.connector import Error

def consultar_produtos():

    query = "SELECT * FROM produtos;"

    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')   
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL!")

            cursor = conexao.cursor()
            cursor.execute(query)

            resultados = cursor.fetchall()

            return resultados

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

    finally:
        # Fecha o cursor e a conexão
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("Conexão encerrada.")

resultados = consultar_produtos()

if resultados:
    for linha in resultados:
        print(linha)
