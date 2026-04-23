def InsertData (name, email, city):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (name, email, city)
    query = "insert into student (name, email, city) values (%s, %s, %s)"
    cursor. execute(query,args)
    conn.commit()
    print("Data inserted")
    conn.close()

n= input("Enter your Name: ")
e= input("Enter your email: ")
c= input("Enter your City: ")

InsertData(n,e,c)
