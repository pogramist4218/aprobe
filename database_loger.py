import psycopg2
from psycopg2 import sql
import file_loger as fl

connect = {
    "dbname": "",
    "user": ",
    "password": "",
    "host": ""
}

def runDBConnection():
    try:
        connection = psycopg2.connect(**connect)
    except Exception as err:
        fl.logError(err)

    connection.autocommit = True
    return connection.cursor()

def cleanDBConnection(conn):
    try:
        conn.close()
    except Exception as err:
        fl.logError(err)

def logInfo(data):
    conn = runDBConnection()
    sql = "INSERT INTO journal (uid, stage, phone, duration, status) VALUES (%(uid)s, %(stage)s, %(phone)s, %(duration)s, %(status)s)"

    try:
        conn.execute(sql, data)
    except Exception as err:
        fl.logError(err)

    cleanDBConnection(conn)
