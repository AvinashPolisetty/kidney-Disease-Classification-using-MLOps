
import mysql.connector

class DatabaseHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='your_host',
            user='your_username',
            password='your_password',
            database='your_database_name'
        )
        self.cursor = self.connection.cursor()

    def insert_prediction(self, image_path, prediction):
        sql_query = "INSERT INTO predictions (image_path, prediction) VALUES (%s, %s)"
        data = (image_path, prediction)

        self.cursor.execute(sql_query, data)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
