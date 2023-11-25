import json
from tkinter.messagebox import showinfo
from database_connect import *
from register import Register
def find_student(students,key):
    for i in students:
        if i.student_id == key:
            return i
    return None
def find_subject(subjects,key):
    for i in subjects:
        if i.subject_id == key:
            return i
    return None


def decode_register(dic):
    if "reg_id" in dic:
        id_reg = dic['reg_id']
        id_sub = dic['subject_id']
        id_stu = dic['student_id']
        time = dic['reg_time']
        return Register(id_reg,id_stu,id_sub,time)
    else:
        return None

class RegisterController:

    def add(self,students,subjects,sub_id,student_id):
        student = find_student(students,student_id)
        subject = find_subject(subjects,sub_id)
        if subject is not None and student is not None:
            return Register(None,student,subject,None)
        else:
            return None
    def read_data(self,students,subjects):
        registers = get_register_from_db()
        itemdelete = []
        # with open('register.json','r+',encoding='UTF-8') as inp:
        #     data = inp.read()
        #     registers = json.loads(data,object_hook=decode_register)
        max = 1000
        for i in registers:
            if i.register_id > max:
                max = i.register_id
        Register.AUTO_ID = max + 1
        for i in registers:
            i.student = find_student(students,i.student)
            i.subject = find_subject(subjects,i.subject)
            if i.subject is None:
                itemdelete.append(i)

        for i in itemdelete:
            registers.remove(i)

        return registers

    def sort_by_time(self,register:list[Register]):
        register.sort(key=lambda x:(x.register_time))

    def sort_by_time_d(self,register:list[Register]):
        register.sort(key=lambda x:(x.register_time),reverse=True)

    def sort_by_id_sub(self,register:list[Register]):
        register.sort(key=lambda x:(x.subject.subject_id))
    def sort_by_id_student(self,register:list[Register]):
        register.sort(key=lambda x:(x.student.student_id))

    def search_by_id_student(self,register,key):
        result = []
        for i in register:
            if i.student.student_id == key:
                result.append(i)
        return result

    def search_by_id_subject(self,register,key):
        result = []
        for i in register:
            if i.subject.subject_id == key:
                result.append(i)
        return result