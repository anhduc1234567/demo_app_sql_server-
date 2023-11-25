import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from exception import GpaError
from student_controller import StudentController
from database_connect import edit_gpa_to_db
class EditGpaView(tkinter.Tk):

    def __init__(self,master,table_student,item,students):
        super(EditGpaView,self).__init__()
        self.resizable(False,False)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.configure(pady=8,padx=8)
        self.master = master
        self.title("Sửa điểm TB")

        self.add_widgets(table_student,item,students)
    def add_widgets(self,table_student,item,students):
        lable_msv = ttk.Label(self,text='Mã SV:').grid(column=0,row=0,sticky=tkinter.W,pady=4,padx=4)
        lable_name = ttk.Label(self,text='Họ và tên:').grid(column=0, row=1,sticky=tkinter.W,pady=4,padx=4)
        lable_gpa= ttk.Label(self,text='Điểm trung bình:').grid(column=0, row=2,sticky=tkinter.W,pady=4,padx=4)

        self.entry_name = ttk.Entry(self)
        self.entry_name.insert(0,table_student.set(item,'c2'))
        self.entry_name.configure(state='disabled')
        self.entry_name.grid(column=1,row=1)

        self.entry_msv = ttk.Entry(self)
        self.entry_msv.insert(0, table_student.set(item,'c4'))
        self.entry_msv.configure(state='disabled')
        self.entry_msv.grid(column=1, row=0)

        self.entry_gpa = ttk.Entry(self)
        self.entry_gpa.grid(column=1, row=2)

        self.btn_save = ttk.Button(self,text='Save',command= lambda: self.com_save(table_student,item,students))
        self.btn_save.grid(column=0,row=3)

        self.btn_cancel = ttk.Button(self, text='Cancel',command=self.destroy)
        self.btn_cancel.grid(column=1, row=3,padx=4,pady=4)

    def com_save(self,table_student,item,students):
        s = StudentController()
        gpa = self.entry_gpa.get().strip()
        try:
            if s.is_gpa_vaild(gpa):
                table_student.set(item,'c7',gpa)

                id = table_student.set(item,'c4')
                for i in students:
                    if i.student_id == id:
                        i.gpa = gpa
                edit_gpa_to_db(id,gpa)
                # s.write_student(students)
                showinfo(message='Thành công')
                # self.master.show_student_in_table()
        except GpaError as e:
            showinfo(message=e)



