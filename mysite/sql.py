from mysql import connector
#connection = connector.connect(user='root', password='root', host='127.0.0.1', database='1db')
class Connection():
   def __init__(self,user,password,host,database):
      self.user=user
      self.password = password
      self.host = host
      self.database = database
      self._connection=None
   @property
   def connection(self):
      return self._connection
   def __enter__(self):
      self.connect()
   def __exit__(self, exc_type, exc_val, exc_tb):
      self.disconnect()
   def connect(self):
      if not self._connection:
         self._connection = connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
   def disconnect(self):
      if self._connection:
         self._connection.close()

class User:
   def __init__(self,db_connection, id, name,age):
       self.db_connection=db_connection.connection
       self.name=name
       self.id=id
       self.age=age
   def save(self):
      c = self.db_connection.cursor()
      c.execute("INSERT INTO users (id, name, age) VALUES (%s,%s,%s)", (self.id, self.name, self.age))
      self.db_connection.commit()
      c.close()
   def spisok(self):
      c = self.db_connection.cursor()
      c.execute("SELECT * FROM users")
      takeall=c.fetchall()
      for e in takeall:
         print(e)
   def tone(self):
      c = self.db_connection.cursor()
      c.execute('SELECT * FROM users WHERE id=(%s)', [(self.id)])
      entries = c.fetchone()
      print(entries)
      self.name = entries[1]
      self.age = entries[2]
      c.close()

conn=Connection('root','root','127.0.0.1','1db')
with conn:
   man=User(conn,'1','fff','27')
   #man.save()
   #man.spisok()
   man.tone()
   print("name: {}, age: {}".format(man.name, man.age))