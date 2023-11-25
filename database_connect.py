import pyodbc
from student import *
from subject import Subject
from register import Register

cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=WHLYANH\SQLEXPRESS;"
            "Database=Students_management;"
            "UID=sa;"
            "PWD=anh15102004;")
cnxn = pyodbc.connect(cnxn_str)

def get_students_from_db():
    SQL = 'SELECT s.CCCD,s.Student_ID,s.Major,s.Email,s.Address,s.Gpa,p.First_Name,p.Mid_Name,p.Last_Name,p.Birth\
    FROM Students s\
    INNER JOIN Persons p\
    ON s.CCCD = p.CCCD'
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    records = cursor.fetchall()
    students = []
    for i in records:
        students.append(Student(i[0],FullName(i[6],i[7],i[8]),Birth(i[9].day,i[9].month,i[9].year),i[4],i[1],i[3],round(i[5], 2),i[2]))
    return students
def get_subjects_from_db():
    SQL = 'SELECT * FROM Subjects'
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    re = cursor.fetchall()
    subjects = []
    for i in re:
        subjects.append(Subject(i[0],i[3],i[1],i[2],i[4]))
    return subjects

def get_register_from_db():
    SQL = 'SELECT * FROM Registers'
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    re = cursor.fetchall()
    registers = []
    for i in re:
        registers.append(Register(i[0],i[2],i[1],str(i[3])))
    return registers
def insert_person_to_db(data):

    sql = 'INSERT INTO Persons(CCCD,First_Name,Mid_Name,Last_Name,Birth)'\
            f'VALUES(\'{data[0]}\',N\'{data[1]}\',N\'{data[2]}\',N\'{data[3]}\',\'{str(data[4])}\')'
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def insert_students_to_db(data):

    sql = 'INSERT INTO Students(Student_ID,CCCD,Email,Address,Gpa,Major)'\
            f'VALUES(\'{data[0]}\',\'{data[1]}\',\'{data[2]}\',N\'{data[3]}\',\'{data[4]}\',N\'{data[5]}\')'
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def insert_subjects_to_db(data):
    sql = 'INSERT INTO Subjects(Subject_Id,Name,Credit,Lesson,Type)' \
          f'VALUES(\'{data[0]}\',N\'{data[1]}\',\'{data[2]}\',\'{data[3]}\',N\'{data[4]}\')'
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()

sql = 'SELECT Subject_Id FROM Subjects Where Subject_Id = 1001 '
cursor = cnxn.cursor()
cursor.execute(sql)
re = cursor.fetchall()

def insert_register_to_db(data):
    sql = 'INSERT INTO Registers(RegisterId,Subject_Id,Student_ID,Time_register)' \
          f'VALUES(\'{data[0]}\',\'{data[1]}\',\'{data[2]}\',\'{data[3]}\')'
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def edit_gpa_to_db(msv,gpa):
    sql = f'UPDATE Students SET Gpa = \'{gpa}\''\
        f'WHERE Student_ID = \'{msv}\''
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def edit_subjects_to_db(subject_id,name,credit,lesson,cate):
    sql = f'UPDATE Subjects SET Name = N\'{name}\',Credit = \'{credit}\',Lesson = \'{lesson}\',Type =  N\'{cate}\'' \
          f'WHERE Subject_Id = \'{subject_id}\''
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def delete_person_from_db(cccd):
    sql = f'DELETE FROM Persons WHERE CCCD = \'{cccd}\' '
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def delete_subject_from_db(subject_id):
    sql = f'DELETE FROM Subjects WHERE Subject_Id = \'{subject_id}\' '
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
def delete_register_from_db(id):
    sql = f'DELETE FROM Registers WHERE RegisterId = \'{id}\' '
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()