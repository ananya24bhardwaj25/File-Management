import mysql.connector

def setup_database():
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    with open('database/create_tables.sql', 'r') as f:
        cursor.execute(f.read(), multi=True)
    with open('database/insert_data.sql', 'r') as f:
        cursor.execute(f.read(), multi=True)
    conn.commit()
    cursor.close()
    conn.close()
def create_user(username, password):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
