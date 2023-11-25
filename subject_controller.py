import json
from tkinter.messagebox import showinfo
from database_connect import *
from subject import Subject
from exception import *
class SubjectEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            "subject_id": o.subject_id,
            "subject_name": o.name,
            "subject_credit": o.credit,
            "subject_lesson": o.lesson,
            "subject_category": o.category
        }
def decode_subject(dic):
    if 'subject_id' in dic:
        ids = dic['subject_id']
        name = dic['subject_name']
        credit = dic['subject_credit']
        lesson = dic['subject_lesson']
        cate = dic['subject_category']
        return Subject(ids,lesson,name,credit,cate)
    else:
        return None
class SubjectController:
    def is_name_vaild(self,name):
        if len(name) < 2 or len(name) > 50:
            raise NameError(name, 'Tên không được quá dài hoặc ngắn')
        for i in name.lower():
            if i.isalnum() is False and i != ' ' and i != '#' and i != '+':
                raise NameError(name, 'Tên không hợp lệ')
        return True

    def add(self,name,credit,lesson,category):
        try:
            self.is_name_vaild(name)
            return Subject(None,int(lesson),name,int(credit),category)
        except NameError as e:
            showinfo(message=e.message)

    def read_subject(self):
        subject = get_subjects_from_db()
        # with open('subject.json','r+',encoding='UTF-8') as inp:
        #     data = inp.read()
        #     subject = json.loads(data,object_hook=decode_subject)
        max = 1000
        for i in subject:
            if i.subject_id > max:
                max = i.subject_id
        Subject.AUTO_ID = max + 1
        return subject

    def write_subject(self,subjects):
        with open('subject.json','w+',encoding='UTF-8') as out:
            data = json.dumps(subjects,ensure_ascii=False,indent=4,cls=SubjectEncoder)
            out.write(data)
    def sort_by_id_sub(self,subject:list[Subject]):
        subject.sort(key= lambda x: (x.subject_id))

    def sort_by_credit(self, subject: list[Subject]):
        subject.sort(key=lambda x: (x.credit),reverse=True)

    def sort_by_lesson(self, subject: list[Subject]):
        subject.sort(key=lambda x: (x.lesson))

    def sort_by_name(self, subject: list[Subject]):
        subject.sort(key=lambda x: (x.name))

    def sort_by_category(self, subject: list[Subject]):
        subject.sort(key=lambda x: (x.category))

    def search_by_name(self,subjects,key):
        result = []
        for i in subjects:
            name = i.name.lower()
            if name.find(key.lower()) != -1:
                print(name)
                result.append(i)
        return result

    def search_by_id(self,subjects,key):
        result = []
        for i in subjects:
            if i.subject_id == key:
                result.append(i)
        return result

    def search_by_credit(self,subjects,key):
        result = []
        for i in subjects:
            if i.credit == key:
                result.append(i)
        return result

    def search_by_lesson(self,subjects,key):
        result = []
        for i in subjects:
            if i.lesson == key:
                result.append(i)
        return result

    def search_by_cate(self,subjects,key):
        result = []
        for i in subjects:
            if i.category == key:
                result.append(i)
        return result


