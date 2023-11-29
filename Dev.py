import sqlite3
conn = sqlite3.connect("School_Database.db")
cursor = conn.cursor()
def Login_Page():
    print("Press 1 for student login")
    print("Press 2 for teacher login")
    print("Press 3 for admin login")
    print("Press 4 to exit")
    l = int(input("Enter your choice: "))
    if l == 1:
        Student_Login()
    elif l == 2:
        Teacher_Login()
    elif l == 3:
        Admin_Login()
    elif l == 4:
        pass 
    else:
        print("Enter valid choice")
def Teacher_Login():
    Employee_ID = input("Enter Employee_ID: ")
    password = input("Enter password: ")
    cursor.execute('''SELECT Password FROM Teacher_Info WHERE Emp_ID = ? ''',(Employee_ID,))
    m = cursor.fetchall()
    if (password,) in m:
        Teacher_Interface()
    else:
        print("Enter right credentials")
def Teacher_Interface():
    print("Press 1 to View Student Table")
    print("Press 2 to Edit Student Table")
    ch = int(input("Enter choice: "))
    if ch == 1:
        cursor.execute('''SELECT * FROM Student_Marks''')
        m = cursor.fetchall()
        for row in m:
            print(row)
    elif ch == 2:
        admn = input("Enter admission number to edit: ")
        cursor.execute('''SELECT Admission_No FROM Student_Info''')
        m = cursor.fetchall()
        if (admn,) in m:
            while True:
                print("Enter Exit to break")
                print("Press 1 to edit Math marks")
                print("Press 2 to edit English marks")
                print("Press 3 to edit Physics marks")
                print("Press 4 to edit Chemistry marks")
                print("Press 5 to edit Computer_Science marks")
                print("Press 6 to edit another admission number: ")
                int0 = input("Enter option: ")
                if int0 == "1":
                    marks = float(input("Enter Math marks: "))
                    cursor.execute('''UPDATE Student_Marks SET Math = ? WHERE Admission_No = ?''',(marks,admn))
                    conn.commit()
                elif int0 == "2":
                    marks = float(input("Enter English marks: "))
                    cursor.execute('''UPDATE Student_Marks SET English = ? WHERE Admission_No = ?''',(marks,admn))
                    conn.commit()
                elif int0 == "3":
                    marks = float(input("Enter Physics marks: "))
                    cursor.execute('''UPDATE Student_Marks SET Physics = ? WHERE Admission_No = ?''',(marks,admn))
                    conn.commit()
                elif int0 == "4":
                    marks = float(input("Enter Chemistry marks: "))
                    cursor.execute('''UPDATE Student_Marks SET Chemistry = ? WHERE Admission_No = ?''',(marks,admn))
                    conn.commit()
                elif int0 == "5":
                    marks = float(input("Enter Computer_Science marks: "))
                    cursor.execute('''UPDATE Student_Marks SET Computer_Science = ? WHERE Admission_No = ?''',(marks,admn))
                    conn.commit()
                elif int0 == "6":
                    admn = input("Enter new admission number: ")
                elif int0 == "Exit" or "exit":
                    break
                cursor.execute('''UPDATE Student_Marks SET Total_Marks = Math + Chemistry + Physics + English + Computer_Science''')
                cursor.execute('''UPDATE Student_Marks SET Percentage = Total_Marks/5''')
                cursor.execute('''UPDATE Student_Marks SET STATUS = "FAIL" WHERE Percentage < 40''')
                cursor.execute('''UPDATE Student_Marks SET STATUS = "PASS" WHERE Percentage >= 40''')
                conn.commit()
        elif (admn,) not in m:
            print("Admission num in not present")
        else:
            print("Enter valid admission number:")
def Student_Login():
    global Admission_No
    Admission_No = input("Enter admission number: ")
    password = input("Enter password: ")
    cursor.execute('''SELECT Password FROM Student_Info WHERE Admission_No = ? ''',(Admission_No,))
    m = cursor.fetchall()
    if (password,) in m:                 
        Student_Interface()
    else:
        print("Enter right credentials")
def Student_Interface():
    global Admission_No
    cursor.execute('''SELECT * FROM Student_Marks WHERE Admission_No = ?''',(Admission_No,))
    m = cursor.fetchall()
    print("Admission_No:", m[0][0])
    print("Name:",m[0][1])                                    
    print("Mathematics", m[0][2])
    print("Physics", m[0][3])
    print("English", m[0][4])
    print("Chemistry", m[0][5])
    print("Computer Science", m[0][6])
    print("Total Score", m[0][7])
    print("Percentage", m[0][8])
    print("Status:", m[0][9])
def testing():
    empid = input("enter empl id: ")
    passw = input("Enter password: ")
    cursor.execute('''SELECT Password FROM Teacher_Info WHERE Emp_ID = ? ''',(empid,))
    m = cursor.fetchall()
    print(m)
    if (passw,) in m:
        print("Yes")
    else:
        print("No")
def Admin_Interface():
    print("Press 1 to edit Student_Info")
    print("Press 2 to insert new admission")
    print("Press 3 to edit Teacher_Info")
    print("Press 4 to insert new teacher")
    print("Enter exit to end")
    ch = input("Enter choice: ")
    if ch == '1':
        edit_student_info()
    elif ch == '2':
        while True:
            Admn = input("Enter new admission number: ")
            Username = input("Enter username: ")
            Name = input("Enter name: ")
            Class = input("Enter class: ")
            Password = input("Enter password: ")
            cursor.execute('''INSERT INTO Student_Info (Admission_No,Username,Name,Class,Password) VALUES(?,?,?,?,?) ''', (Admn, Username, Name,Class, Password,))
            conn.commit()
            inp = input("Press Y to continue and N to break: ")
            if inp == "N":
                break
    elif ch == '3':
        edit_teacher_info()
    elif ch == '4':
        Empid = input("Enter new employee id: ")
        Username = input("Enter username: ")
        Name = input("Enter name: ")
        Class = input("Enter class: ")
        Password = input("Enter password: ")
        cursor.execute('''INSERT INTO Teacher_Info (Emp_ID,Username,Name,Class,Password) VALUES(?,?,?,?,?) ''', (Empid, Username, Name, Class, Password,))
        conn.commit()
    elif ch == '5':
        pass
    
def edit_student_info():
    inp = input("Enter Admission_No you want to edit: ")
    cursor.execute('''SELECT * FROM Student_Info WHERE Admission_No = ?''',(inp,))
    result = cursor.fetchall()
    if (inp,) in result:
        while True:
            print("Type exit to break")
            inp0 = input("Enter column_name to edit: ")
            cursor.execute('''PRAGMA table_info(Student_Info)''')
            columns = cursor.fetchall()
            if (inp0,) in columns:
                inp1 = input("Enter value to edit: ")
                cursor.execute('''UPDATE Student_Info SET {} = ? WHERE Admission_No = ? ''',format(inp0),(inp1,inp,))
                conn.commit()
            elif inp0 == "Exit" or inp0 == "exit":
                break
    elif (inp,) not in result:
        print("Enter valid admission_No")
def edit_teacher_info():
    inp = input("Enter Employee ID you want to edit: ")
    cursor.execute('''SELECT * FROM Teacher_Info WHERE Emp_ID = ?''',(inp,))
    result = cursor.fetchall()
    if (inp,) in result:
        while True:
            print("Type exit to break")
            inp0 = input("Enter column_name to edit: ")
            cursor.execute('''PRAGMA table_info(Student_Info)''')
            columns = cursor.fetchall()
            if (inp0,) in columns:
                inp1 = input("Enter value to edit: ")
                cursor.execute('''UPDATE Teacher_Info SET {} = ? WHERE Emp_ID = ? ''',format(inp0),(inp1,inp,))
                conn.commit()
            elif inp0 == "Exit" or inp0 == "exit":
                break
    elif (inp,) not in result:
        print("Enter valid employee id")
def Admin_Login():
    username = "Admin"
    password = "Admin"
    userinp = input("Enter username: ")
    passinp = input("Enter password:")
    if userinp == username and passinp == password:
        Admin_Interface()
    else:
        print("Enter correct credentials")

Login_Page()
