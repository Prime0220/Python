import sqlite3

con = sqlite3.connect("C:\\Users\\User\\Desktop\\DBPython\\210421_DBPython")
cur = con.cursor()
'''
cur.execute("CREATE TABLE StudentTB (Student_ID str, Student_Name str, Student_Email str, Student_Birth Student int)")
'''
while (True) :
    Student_ID = input("학번 입력 : ")
    if Student_ID == "" :
        break
    Student_Name = input("이름 입력 : ")
    Student_Email = input("e-mail 입력 : ")
    Student_Birth = input("출생년도 입력 : ")
    sql = "INSERT INTO StudentTB VALUES('" + Student_ID + "', '" + Student_Name + "', '" + Student_Email + "', " + Student_Birth + ")"
    cur.execute(sql)
    
con.commit()

cur.execute("SELECT * FROM studentTB")
print("학번 / 이름 / 이메일 / 출생연도")

while (True) :
    row = cur.fetchone()
    if row == None :
        break
    Student_ID  = row[0]
    Student_Name = row[1]
    Student_Email = row[2]
    Student_Birth = row[3]
    print("%s / %s / %s / %8d" %(Student_ID, Student_Name, Student_Email, Student_Birth))
    
con.close()
    
