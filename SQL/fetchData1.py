import configparser
import psycopg2
import mysql.connector

config = configparser.ConfigParser()
config.read('SQL/.secrets')

DB_HOST = config['DEFAULT']['DB_HOST']
DB_NAME = config['DEFAULT']['DB_NAME']
DB_USER = config['DEFAULT']['DB_USER']
DB_PASS = config['DEFAULT']['DB_PASS']
DB_PORT = config['DEFAULT']['DB_PORT']

# for PostgreSQL
db1 = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

# for MySQL
myDB = mysql.connector.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

query = "SELECT * FROM employees;"
cursor = myDB.cursor()
cursor.execute(query)
result = cursor.fetchall()
print(result)
