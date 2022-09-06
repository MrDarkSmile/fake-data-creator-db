import sqlite3, time
from faker import Faker
con = sqlite3.connect("data.db")
c = con.cursor()

f = Faker("fa_IR")

sql = """CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name Text(100) ,
    email Text(100) ,
    address Text(300) ,
    job Text(100),
    bank Text(100),
    ip Text(50),
    mac Text(100)
    )"""
try:
  c.execute(sql)
  con.commit()
  print("database created")
except:
  con.rollback()
  print("database is exist")

marz = int(input("enter the number of data => "))

n=0
t1 = time.time()

while n != marz:
  sql = f"INSERT INTO users(name,email,address,job,bank,ip,mac) VALUES ('{f.name()}','{f.email()}','{f.address()}','{f.job()}','{f.bank()}','{f.ipv4()}','{f.mac_address()}')"
  c.execute(sql)
  con.commit()
  n+=1
  


t2 = time.time()
t = t2-t1
print(t)
