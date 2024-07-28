import mysql.connector

def create_file(name, directory_id, size):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Files (name, directory_id, size) VALUES (%s, %s, %s)", (name, directory_id, size))
    conn.commit()
    cursor.close()
    conn.close()

def delete_file(file_id):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Files WHERE file_id = %s", (file_id,))
    conn.commit()
    cursor.close()
    conn.close()

def update_file(file_id, name=None, size=None):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE Files SET name = %s WHERE file_id = %s", (name, file_id))
    if size:
        cursor.execute("UPDATE Files SET size = %s WHERE file_id = %s", (size, file_id))
    conn.commit()
    cursor.close()
    conn.close()
 import mysql.connector

def create_file(name, directory_id, size):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Files (name, directory_id, size) VALUES (%s, %s, %s)", (name, directory_id, size))
    conn.commit()
    cursor.close()
    conn.close()

def delete_file(file_id):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Files WHERE file_id = %s", (file_id,))
    conn.commit()
    cursor.close()
    conn.close()

def update_file(file_id, name=None, size=None):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE Files SET name = %s WHERE file_id = %s", (name, file_id))
    if size:
        cursor.execute("UPDATE Files SET size = %s WHERE file_id = %s", (size, file_id))
    conn.commit()
    cursor.close()
    conn.close()

import mysql.connector

def create_directory(name, parent_directory_id=None):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Directories (name, parent_directory_id) VALUES (%s, %s)", (name, parent_directory_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_directory(directory_id):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Directories WHERE directory_id = %s", (directory_id,))
    conn.commit()
    cursor.close()
    conn.close()
