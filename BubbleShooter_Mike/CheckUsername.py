import sqlite3

def CheckUsername():
    connect=sqlite3.connect('Username_Password_Database')
    cursor=connect.cursor()
    cursor.execute(
       'SELECT * FROM Username_Password_Table'
    )
    connect.close()


print(CheckUsername())