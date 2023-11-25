import datetime
class Register:
    AUTO_ID = 1000
    def __init__(self,register_id,student,subject,register_time):
        if register_id is None:
            self.__register_id = Register.AUTO_ID
            Register.AUTO_ID += 1
        else:
            self.__register_id = register_id
        self.__student = student
        self.__subject = subject
        if register_time is None:
            time_date = datetime.datetime.now()
            format = '%Y-%m-%d  %H:%M:%S'
            self.__register_time = datetime.datetime.strptime(time_date.strftime(format), format)
        else:
            format = '%Y-%m-%d  %H:%M:%S'
            self.__register_time = datetime.datetime.strptime(register_time,format)
    @property
    def register_id(self):
        return self.__register_id
    @register_id.setter
    def register_id(self,value):
        self.__register_id = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        self.__register_time = value
