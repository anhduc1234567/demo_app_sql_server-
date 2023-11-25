import re
from exception import *
from tkinter.messagebox import showinfo
from student import *
import json
from database_connect import *
class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            'person_id':o.id,
            'full_name':{
                "first": o.name.first,
                "last": o.name.last,
                "mid": o.name.mid
            },
            'birth_date':{
                  "day": o.birth.day,
                  "month": o.birth.month,
                  "year": o.birth.year
            },
            "address": {
                "wards": o.address.wards,
                "district": o.address.district,
                "city": o.address.city
            },
            "student_id": o.student_id,
            "email": o.email,
            "major": o.major,
            "gpa": o.gpa
        }

def decode_full_name(dic):
    if 'first' in dic:
        return FullName(dic['first'], dic['mid'], dic['last'])
    else:
        return None


def decode_birth(dic):
    if 'day' in dic:
        return Birth(dic['day'], dic['month'], dic['year'])
    else:
        return None


def decode_address(dic):
    if 'wards' in dic:
        return Address(dic['wards'], dic['district'], dic['city'])
    else:
        return None

def decode_student(dic):
    if 'person_id' in dic:
        id = dic['person_id']
        full_name = decode_full_name(dic['full_name'])
        birth = decode_birth(dic['birth_date'])
        address = decode_address(dic['address'])
        student_id = dic['student_id']
        email = dic['email']
        major = dic['major']
        gpa = dic['gpa']
        return Student(id,full_name,birth,address,student_id,email,gpa,major)
    else:
        return dic
class StudentController:
    def is_name_vaild(self,name):
        if len(name) < 2 or len(name) > 50:
            raise NameError(name, 'Tên không được quá dài hoặc ngắn')
        for i in name.lower():
            if i.isalpha() is False and i != ' ':
                raise NameError(name, 'Tên không hợp lệ')
        return True

    def is_address_vaild(self,address):
        for i in address.lower():
            if i.isalpha() is False and i != ' ' and i != ',':
                raise AddressError(address, 'Địa chỉ không không hợp lệ')
        return True

    def is_birth_vaild(self,birth:str):
        pattern = r'^(0[1-9]|[1-2][0-9]|[3][0-1])/(0[1-9]|1[0-2])/\d{4}$'
        # pattern = r'^(0[1-9]|[12][0-9]|[3][0-1])/(0[1-9]|1[0-2])/\d{4}$'
        matcher = re.match(pattern,birth.strip())
        if matcher :
            return True
        else:
            raise BirthError(birth,'Ngày sinh không hợp lệ')

    def is_gpa_vaild(self,grade):
        if len(grade.strip()) == 0:
            raise GpaError(grade, 'Điểm không được trống')
        pattern = '^\\d{1}.\\d{1,2}$'
        if re.match(pattern, grade) and 0.0 < float(grade) < 4.0:
            return True
        raise GpaError(grade, 'Điểm không hợp lệ')
    def is_email_vaild(self,email):
        pattern = '^[a-z_]+[a-z]+[0-9._-]*@[a-z0-9]+.[a-z]{2,4}$'
        matcher = re.match(pattern, email, flags=re.IGNORECASE)
        if matcher:
            return True
        else:
            raise EmailError(email,'Email không hợp lệ')


    def add(self,person_id,name,birth,email,gpa,major,address):
        try:
            self.is_name_vaild(name)
            self.is_email_vaild(email)
            self.is_gpa_vaild(gpa)
            self.is_birth_vaild(birth)
            self.is_address_vaild(address)
            names = name.split()
            full_name = None
            if len(names) == 1:
                full_name = FullName(names[0],' ',' ')
            elif len(names) == 2:
                full_name = FullName(names[0],' ',names[1])
            else:
                mid = ''
                for i in range(1,len(names) - 1):
                    mid = mid + names[i] + ' '
                full_name = FullName(names[0],mid,names[len(names) - 1])
            birthes = birth.split('/')
            birth_date = Birth(birthes[0],birthes[1],birthes[2])
            add_ress = None
            addresses = address.split(',')
            if len(addresses) == 1:
                add_ress = Address(' ',addresses[0],' ')
            elif len(addresses) == 2:
                add_ress = Address(addresses[0],' ',addresses[1])
            else:
                district = ''
                for i in range(1,len(addresses) - 1):
                    district = district + addresses[i] + ' '
                add_ress = Address(addresses[0],district,address[len(addresses) - 1])
            return Student(person_id,full_name,birth_date,add_ress,None,email,float(gpa),major)
        except NameError as e:
            showinfo(message=e.message)
        except EmailError as e:
            showinfo(message=e.message)
        except GpaError as e:
            showinfo(message=e.message)
        except BirthError as e:
            showinfo(message=e.message)

    def read_student(self):
        # students = []
        students = get_students_from_db()
        # with open('student.json','r+',encoding='UTF-8') as inp:
        #     data = inp.read()
        #     students = json.loads(data,object_hook=decode_student)
        max = 1000
        for i in students:
            if int(i.student_id[2:]) > max:
                max = int(i.student_id[2:])
        Student.AUTO_ID = max + 1
        # self.write_student(students)
        return students

    def sort_by_name(self,students:list[Student]):
        students.sort(key= lambda x:(x.name.first))

    def sort_by_name_first(self,students:list[Student]):
        students.sort(key= lambda x:(x.name.first,x.name.last))
    def sort_by_gpa(self,students:list[Student]):
        students.sort(key= lambda x:(float(x.gpa)))

    def sort_by_birth(self,students:list[Student]):
        students.sort(key= lambda x:(x.birth),reverse=True)

    def search_by_name(self,students,key):
        # students = self.read_student()
        result = []
        for i in students:
            name = i.name.first + ' ' + i.name.mid + ' ' + i.name.last
            name = name.lower()
            if name.find(key) != -1 :
                print(name)
                result.append(i)
        return result

    def search_by_gpa(self,students,key):
        result = []
        for i in students:
            if i.gpa == float(key):
                result.append(i)
        return result

    def search_by_birth_day(self,students,key):
        result = []
        for i in students:
            if i.birth.day == int(key):
                result.append(i)
        return result
    def search_by_birth_month(self,students,key):
        result = []
        for i in students:
            if i.birth.month == int(key):
                result.append(i)
        return result
    def write_student(self,students):
        with open('student.json','w+',encoding='UTF-8') as out:
            data = json.dumps(students,ensure_ascii=False,indent=4,cls=StudentEncoder)
            out.write(data)

    def search_by_birth_year(self,students,key):
        result = []
        for i in students:
            if i.birth.year == int(key):
                result.append(i)
        return result