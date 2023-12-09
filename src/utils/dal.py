import mysql.connector


class DAL:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="vacations")

    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table


    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar

    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            last_row_id = cursor.lastrowid
            return last_row_id

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

    def close(self):
        self.connection.close()
