import mysql.connector as a
con = a.connect(host="localhost",
                 user ="root",
                 password ="1234",
                 database ="Asus")
def cars():

    n = input("Enter Car Model Name : ")
    e = input("Enter Engine Type : ")
    f = input("Enter Fuel Type : ")
    s = input("Enter Segment : ")
    m = input("Enter Mileage : ")
    p = input("Enter Price : ")
    data = ( n, e, f, s, m, p)
    sql = 'insert into cars values( %s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data inserted cars table successfully")
    main()

def carDetails():
    sql = " select * from cars"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def employee():

    id = input("Enter Employee Id : ")
    n = input("Enter Employee Name : ")
    p = input("Enter Employee Position : ")
    c = input("Enter Employee contact : ")
    a = input("Enter Employee Address : ")
    s = input("Enter Employee Salary : ")
    data = (id, n, p, c, a, s)
    sql = 'insert into Employee values( %s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data inserted in Employee table successfully")
    main()

def employeeDetails():
    sql = " select * from Employee"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def searchCarByName():
    ec = input("Enter Car Model Name : ")
    v = (ec,)
    sql = "select * from cars where model = %s "
    c = con.cursor()
    c.execute(sql,v)
    bs = c.fetchone()
    print(bs)
    main()

def searchEmployeeByName():
    ec = input("Enter Employee Name : ")
    v = (ec,)
    sql = "select * from employee where name = %s "
    c = con.cursor()
    c.execute(sql,v)
    bs = c.fetchone()
    print(bs)
    main()


def main():
    print("""
    1.Add new Car Details
    2.Display Car Details
    3.Add New Employee Details
    4.Display Employee Details
    5.Search Car by Name
    6.Search Employee by Name
    """)
    choice = input("Enter Task : ")
    while True:
        if(choice == '1'):
            cars()
        elif(choice=='2'):
            carDetails()
        elif(choice=='3'):
            employee()
        elif(choice =='4'):
            employeeDetails()
        elif(choice == '5'):
            searchCarByName()
        elif(choice == '6'):
            searchEmployeeByName()

        else:
            print("Wrong Choice..")
main()



