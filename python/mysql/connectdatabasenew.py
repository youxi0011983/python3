import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="229183",
    #auth_plugin='mysql_native_password'
)

print(mydb)

mycursor = mydb.cursor()

print(mycursor)


mycursor.execute("USE mysql")
 
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
