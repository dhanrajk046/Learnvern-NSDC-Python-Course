# LECTURE 2
# import pymysql

# def CreateConn():
#     return pymysql.connect(host="localhost",database="learnvern", user="root", password="zhfs4866@#AB",port=3306)

# def CreateTable():
#     conn = CreateConn()
#     cursor = conn.cursor()
#     query = "CREATE TABLE IF NOT EXISTS student (sid int primary key auto_increment, name VARCHAR(50), email VARCHAR(50), city VARCHAR(50))"

#     cursor.execute(query)
#     conn.commit()
#     print("Table Created")
#     conn.close()

# CreateTable()

# def InsertData (name, email, city):
#     conn = CreateConn()
#     cursor = conn.cursor()
#     args = (name, email, city)
#     query = "insert into student (name, email, city) values (%s, %s, %s)"
#     cursor. execute(query,args)
#     conn.commit()
#     print("Data inserted")
#     conn.close()

# n= input("Enter your Name: ")
# e= input("Enter your email: ")
# c= input("Enter your City: ")

# InsertData(n,e,c)

# LECTURE 3
# import pymysql

# def CreateConn():
#     return pymysql.connect(host="localhost",database="Learnvern",user = "root", password = "zhfs4866@#AB", port = 3306)

# def showAllData():
#     conn = CreateConn()
#     cursor = conn.cursor()
#     query = "select * from student"
#     cursor.execute(query)
#     result = cursor.fetchall()
#     for i in result:
#         print(i)

# def showAllDatabyid(sid):
#     conn = CreateConn()
#     cursor = conn.cursor()
#     args = (sid)
#     query = "select * from student where sid = %s"
#     cursor.execute(query,args)
#     result = cursor.fetchall()
#     for i in result:
#         print(i)

# showAllData()
# sid = int(input("Enter your Id: "))
# showAllDatabyid(sid)


# LECTURE 4
import pymysql


def CreateConn():
    return pymysql.connect(
        host="localhost",
        database="Learnvern",
        user="root",
        password="zhfs4866@#AB",
        port=3306,
    )


def showAllData():
    conn = CreateConn()
    cursor = conn.cursor()
    query = "select * from student"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)


# def UpdateData(name, email, city, sid):
#     conn = CreateConn()
#     cursor = conn.cursor()
#     args = (name, email, city, sid)
#     query = "update student set name = %s, email = %s, city = %s where sid = %s"
#     cursor.execute(query, args)
#     conn.commit()
#     print("Data Updated")
#     print("Data Updated")
#     conn.close()


# sid = int(input("enter your id: "))
# n = input("Enter your Name: ")
# e = input("Enter your Email: ")
# c = input("Enter your City: ")

# UpdateData(n, e, c, sid)

def DeleteData(sid):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (sid)
    query = "delete from student where sid = %s"
    cursor.execute(query,args)
    conn.commit()
    print("Data Deleted")
    conn.close()

showAllData()

sid = int(input("Enter your id: "))

DeleteData(sid)

showAllData()