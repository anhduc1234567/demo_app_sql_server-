import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

from  subject_controller import SubjectController
from subject import Subject
from database_connect import edit_subjects_to_db
class AddSubjectView(tkinter.Tk):
    def __init__(self,master):
        super(AddSubjectView,self).__init__()
        self.mastter = master
        self.title('Create new subject')
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.var_name = tkinter.StringVar()
        self.var_lesson = tkinter.StringVar()
        self.configure(padx=8,pady=8)
        self.add_widgets()

    def add_widgets(self):
        ttk.Label(self,text='Tên môn học:').grid(column=0,row=0,padx=4,pady=4)
        ttk.Label(self,text='Số tiết học:').grid(column=0,row=1,padx=4,pady=4)
        ttk.Label(self,text='Số tín chỉ:').grid(column=0,row=2,padx=4,pady=4)
        ttk.Label(self,text='Loại môn học:').grid(column=0,row=3,padx=4,pady=4)

        self.entry_name = ttk.Entry(self,textvariable=self.var_name)
        self.entry_name.grid(column=1,row=0,pady=4,padx=4,sticky=tkinter.EW)
        self.lesson = ttk.Entry(self,textvariable=self.var_lesson)
        self.lesson.grid(column=1,row=1,pady=4,padx=4,sticky=tkinter.EW)
        credit = []
        for i in range(2,14):
            credit.append(str(i))
            i += 1

        self.credit = ttk.Combobox(self,values=credit,height=5,width=20)
        self.credit.current(0)
        self.credit.grid(column=1,row=2,pady=4,padx=4,sticky=tkinter.EW)

        cate = ['Cơ sở ngành','Tự chọn','Cơ bản','Chuyên ngành', 'Nâng cao']
        self.category = ttk.Combobox(self,values=cate,height=5)
        self.category.grid(column=1,row=3,pady=4,padx=4,sticky=tkinter.EW)
        self.category.current(0)

        self.btn_ok = ttk.Button(self,text='Save',command=self.com_create_subject)
        self.btn_ok.grid(column=1,row=4,pady=8,sticky=tkinter.N)

        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_cancel.grid(column=0, row=4, pady=8, sticky=tkinter.N)

    def com_create_subject(self):
        name = self.entry_name.get()
        lesson = self.lesson.get()
        credit = self.credit.get()
        category = self.category.get()
        s = SubjectController()
        if len(name) == 0:
            showinfo(message='Lỗi tên không được trống')
        elif len(lesson) == 0:
            showinfo(message='Lỗi số tiết không đuợc để trống')
        elif lesson.isdigit() is False:
            showinfo(message='Số tiết phải là số nguyên')
        elif int(lesson) > 54 or int(lesson) < 1:
            showinfo(message='Số tiết phải nằm trong khoảng 1 - 54')
        else:
            subject = s.add(name,credit,lesson,category)
            if subject is not None:
                self.mastter.add_new_subject(subject)
                showinfo(message='Tạo môn học thành công')

class EditSubjectView(tkinter.Tk):
    def __init__(self,table,item,subjects):
        super(EditSubjectView,self).__init__()
        # self.mastter = master
        self.title('Edit subject')
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.var_name = tkinter.StringVar()
        self.var_lesson = tkinter.StringVar()
        self.configure(padx=8,pady=8)
        self.add_widgets(table,item,subjects)

    def add_widgets(self,table,item,subjects):
        ttk.Label(self,text='Mã môn học: ').grid(column=0,row=0,pady=4,padx=4)
        ttk.Label(self,text='Tên môn học:').grid(column=0,row=1,padx=4,pady=4)
        ttk.Label(self,text='Số tiết học:').grid(column=0,row=2,padx=4,pady=4)
        ttk.Label(self,text='Số tín chỉ:').grid(column=0,row=3,padx=4,pady=4)
        ttk.Label(self,text='Loại môn học:').grid(column=0,row=4,padx=4,pady=4)


        self.entry_id = ttk.Entry(self)
        self.entry_id.grid(column=1,row=0,padx=4,pady=4,sticky=tkinter.EW)
        self.entry_id.insert(0,table.set(item,'c1'))
        self.entry_id.configure(state='disabled')

        self.entry_name = ttk.Entry(self,textvariable=self.var_name)
        self.entry_name.grid(column=1,row=1,pady=4,padx=4,sticky=tkinter.EW)
        self.entry_name.insert(0,table.set(item,'c2'))

        self.lesson = ttk.Entry(self,textvariable=self.var_lesson)
        self.lesson.grid(column=1,row=2,pady=4,padx=4,sticky=tkinter.EW)
        self.lesson.insert(0,table.set(item,'c4'))

        credit = []
        for i in range(2,14):
            credit.append(str(i))
            i += 1

        self.credit = ttk.Combobox(self,values=credit,height=5,width=20)
        self.credit.current(int(table.set(item,'c3'))-2)
        self.credit.grid(column=1,row=3,pady=4,padx=4,sticky=tkinter.EW)

        cate = ['Cơ sở ngành','Tự chọn','Cơ bản','Chuyên ngành', 'Nâng cao']
        self.category = ttk.Combobox(self,values=cate,height=5)
        self.category.grid(column=1,row=4,pady=4,padx=4,sticky=tkinter.EW)
        index = 0
        for i in range(0,len(cate)):
            if cate[i] == table.set(item,'c5'):
                index = i
        self.category.current(index)

        self.btn_ok = ttk.Button(self,text='Save',command=lambda: self.com_edit_subject(table,item,subjects))
        self.btn_ok.grid(column=1,row=5,pady=8,sticky=tkinter.N)

        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_cancel.grid(column=0, row=5, pady=8, sticky=tkinter.N)

    def com_edit_subject(self,table,item,subjects):
        name = self.entry_name.get()
        lesson = self.lesson.get()
        credit = self.credit.get()
        category = self.category.get()
        s = SubjectController()
        if len(name) == 0:
            showinfo(message='Lỗi tên không được trống')
        elif len(lesson) == 0:
            showinfo(message='Lỗi số tiết không đuợc để trống')
        elif lesson.isdigit() is False:
            showinfo(message='Số tiết phải là số nguyên')
        elif int(lesson) > 54 or int(lesson) < 1:
            showinfo(message='Số tiết phải nằm trong khoảng 1 - 54')
        else:
            table.set(item,'c2',name)
            table.set(item,'c3',credit)
            table.set(item,'c4',lesson)
            table.set(item,'c5',category)
            id = table.set(item,'c1')
            for i in subjects:
                if i.subject_id == int(id):
                    i.name = name
                    i.credit = credit
                    i.lesson = lesson
                    i.category = category
            # s.write_subject(subjects)
            edit_subjects_to_db(id,name,credit,lesson,category)
            showinfo(message='Sửa thành công')






