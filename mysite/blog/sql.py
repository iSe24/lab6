from mysql import connector
connection = connector.connect(user='root', password='root', host='127.0.0.1', database='1db')
def save(id, name, age):
   id = id
   name = name
   age = age
   c = connection.cursor()
   c.execute("INSERT INTO users (id, name, age) VALUES (%s,%s,%s)",(id, name, age))
   connection.commit()
   c.close()

try:
   c = connection.cursor()
   c.execute("SELECT * from users;")
   take = c.fetchall()
   for e in take:
       print(e)
   c.execute("SELECT name from users WHERE age>=20;")
   take = c.fetchall()
   for e in take:
       print(e[0])
   pass
finally:
   connection.close()



