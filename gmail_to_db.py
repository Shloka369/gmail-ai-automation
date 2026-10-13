import mysql.connector

def insert_task(subject, body):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shloka",
        database="email_tasks_db"
    )

    cursor = conn.cursor()

    sql = """
    INSERT INTO tasks (title, description, priority)
    VALUES (%s, %s, %s)
    """

    values = (subject, body[:1000], "medium")  # limit body length

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()
