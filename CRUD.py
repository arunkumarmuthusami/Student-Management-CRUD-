import pymysql
#from tabulate import Tabulate
con = pymysql.connect(host="localhost", user="root", password="root", database="Student_Management")


def insert(student_name,age,Gender,DOB,department,contact,email,address,zipcode):
    res = con.cursor()
    sql = "insert into student_details (student_name,age,Gender,DOB,department,contact,email,address,zipcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    details= (student_name,age,Gender,DOB,department,contact,email,address,zipcode)
    res.execute(sql,details)
    con.commit()
    print("Insert Data Successfully")


def update(student_name,age,Gender,DOB,department,contact,email,address,zipcode,id):
    res = con.cursor()
    sql = "update student_details set student_name=%s,age=%s,Gender=%s,DOB=%s,department=%s,contact=%s,email=%s,address=%s,zipcode=%s where id=%s"
    details= (student_name,age,Gender,DOB,department,contact,email,address,zipcode)
    res.execute(sql,details)
    con.commit()
    print("Update Data Successfully")



def select():
    res = con.cursor()
    sql = "SELECT id,student_name,age,Gender,DOB,department,contact,email,address,zipcode from student_details"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(result)


def delete(id):
    res = con.cursor()
    sql = "delete from student_details where id=%s"
    details = (id,)
    res.execute(sql, details)
    con.commit()
    print("Delete Data Successfully")


while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        #id=int(input("Enter your ID : "))
        student_name = input("Enter Name : ")
        age = input("Enter Age : ")
        Gender = input("Enter Gender : ")
        DOB = input("Enter DOB : ")
        department = input("Enter Department : ")
        contact = input("Enter Contact No :")
        email = input("Enter Mail_ID :")
        address = input("Enter Your Location :")
        zipcode = input("Enter zipcode :")
        insert(student_name,age,Gender,DOB,department,contact,email,address,zipcode)

    elif choice == 2:
        id =int(input("Enter your ID  : "))
        student_name = input("Enter Name : ")
        age = input("Enter Age : ")
        Gender = input("Enter Gender : ")
        DOB = input("Enter DOB : ")
        department = input("Enter Department : ")
        contact = input("Enter Contact No :")
        email = input("Enter Mail_ID:")
        address = input("Enter Your Location :")
        zipcode = input("Enter zipcode:")
        update(student_name,age,Gender,DOB,department,contact,email,address,zipcode,id)

    elif choice == 3:
        select()

    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)

    elif choice == 5:
        quit()

    else:
        print("Invalid Selection . Please Try Again!")