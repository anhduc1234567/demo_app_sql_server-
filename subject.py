class Subject:
    AUTO_ID = 1000
    def __init__(self,subject_id,lesson,name,credit,category):
        if subject_id is not None:
            self.__subject_id = subject_id
        else:
            self.__subject_id = Subject.AUTO_ID
            Subject.AUTO_ID +=1
        self.__name = name
        self.__credit = credit
        self.__lesson = lesson
        self.__category = category
    @property
    def subject_id(self):
        return self.__subject_id
    @subject_id.setter
    def subject_id(self,value):
        self.__subject_id = value

    @property
    def lesson(self):
        return self.__lesson

    @lesson.setter
    def lesson(self, value):
        self.__lesson = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,value):
        self.__credit = value

    def __str__(self):
        return f'{self.subject_id} {self.name}'