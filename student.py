# from datetime import date
class FullName:
    def __init__(self,first,mid,last):
        self.__first = first
        self.__mid = mid
        self.__last = last
    @property
    def first(self):
        return self.__first
    @first.setter
    def first(self,value):
        self.__first = value
    @property
    def mid(self):
        return self.__mid
    @mid.setter
    def mid(self,value):
        self.__mid = value
    @property
    def last(self):
        return self.__last
    @last.setter
    def last(self,value):
        self.__last = value

    def __str__(self):
        return f'{self.first} {self.mid} {self.last}'

class Birth:
    def __init__(self,d,m,y):
        self.__day = d
        self.__month = m
        self.__year = y
    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self,value):
        self.__day = value
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self,value):
        self.__month = value
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value

    def __gt__(self, other):
        if self.day > other.day and self.month == other.month and self.year == other.year:
            return True
        elif self.month > other.month and self.year == other.year:
            return True
        elif self.year > other.year:
            return True
        return False

    def __lt__(self, other):
        if self.day < other.day and self.month == other.month and self.year == other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif self.year < other.year:
            return True
        return False

    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

class Address :
    def __init__(self,wards,district,city):
        self.__wards = wards
        self.__district = district
        self.__city = city
    @property
    def wards(self):
        return self.__wards
    @wards.setter
    def wards(self,value):
        self.__first = value
    @property
    def district(self):
        return self.__district
    @district.setter
    def district(self,value):
        self.__mid = value
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,value):
        self.__city = value

    def __str__(self):
        return f'{self.wards} {self.district} {self.city}'
class Person:
    def __init__(self,id,name,birth,address):
        self.__id = id
        self.__name = name
        # fomat = '%d/%m/%Y'
        self.__birth = birth
        self.__address = address


    def setBirth(self,birth):
        b = birth.strip().split('/')
        return Birth(int(b[2]),int(b[1]),int(b[0]))
    def setName(self,name:str):
        words = name.strip().split()
        first = words[0]
        last = words[len(words) - 1]
        mid = ''
        for i in range(1,len(words)- 1):
            mid += words[i] + ' '
        return FullName(first,mid,last)

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address = value

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth = value



class Student(Person):
    AUTO_ID = 1000
    def __init__(self,person_id,name,birth,address,student_id,email,gpa,major):

        super().__init__(person_id,name,birth,address)

        if student_id is None:
            self.__student_id = f'SV{Student.AUTO_ID}'
            Student.AUTO_ID += 1
        else:
            self.__student_id = student_id
        self.__email = email
        self.__gpa = gpa
        self.__major = major


    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    def __str__(self):
        return f'Student {self.student_id} {self.email}'