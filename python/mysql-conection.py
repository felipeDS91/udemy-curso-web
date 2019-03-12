# First we need instal mysql and mysql python connector from mysql.com
import mysql.connector
cnx = mysql.connector.connect(user='supervisor', password='SISADMIN1107', host='127.0.0.1', database='aaa')
cursor = cnx.cursor()

query = ("select codigo, descricao, enviado from teste")

cursor.execute(query)

for (codigo, descricao, enviado) in cursor:
  print(codigo, descricao, enviado)

cursor.close()
cnx.close()


# Example with filter date
'''
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()

'''
