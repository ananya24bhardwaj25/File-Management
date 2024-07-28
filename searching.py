import mysql.connector

def search_files(keyword):
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='file_system')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Files WHERE name LIKE %s", ('%' + keyword + '%',))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
