import sqlite3
from sqlite3 import Error

class SqlLiteDS():

    """
        SQLLite datasource for passwdMgr.
    """

    def __init__(self):
        self.connection = self.create_connection("db")

    def getConnection(self):
        return self.connection

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)

        except Error as e:
            print(e)

        return conn

    def login(self, username):
        cursor = self.connection.cursor()

        login = cursor.execute(f"select * from Users where username = \"{username}\"").fetchone()

        cursor.close()

        if login:
            return (login[1], login[2], True)

    def getBlob(self, username):
        cursor = self.connection.cursor()

        blob = cursor.execute(f"select * from User_sites WHERE username = \"{username}\"").fetchone()
        cursor.close()

        return blob[3]

    def saveBlob(self, blob, username):
        cursor = self.connection.cursor()
        cursor.execute(f"UPDATE User_sites SET sites = \"{blob}\" WHERE username = \"{username}\"")
        self.connection.commit()
        

    def getAllUsers(self):
        cursor = self.connection.cursor()
        all = cursor.execute("select * from Users;").fetchall()
        cursor.close()

        return all

if __name__ == "__main__":
    connection = SqlLiteDS()
    obj = connection.getAllUsers()

    for users in obj:
        print(users[1])
