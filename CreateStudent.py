from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo
from student_controller import StudentController

class AddStudentView(tkinter.Tk):
    def __init__(self,master):
        super(AddStudentView,self).__init__()
        self.mastter = master
        self.title('Add new student')
        self.configure(padx=16,pady=8)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.var_cccd = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_birth = tkinter.StringVar()
        self.var_gpa = tkinter.StringVar()
        self.var_major = tkinter.StringVar()
        self.var_address = tkinter.StringVar()
        self.student = None
        self.add_widgets()
    def add_widgets(self):
        ttk.Label(self,text='CCCD:').grid(column=0,row=0,sticky=tkinter.W,pady=8)
        ttk.Label(self,text='Họ và tên:').grid(column=0, row=1, sticky=tkinter.W,pady=8)
        ttk.Label(self,text='Ngày sinh:').grid(column=0, row=2, sticky=tkinter.W,pady=8)
        ttk.Label(self,text='Email:').grid(column=0, row=3, sticky=tkinter.W,pady=8)
        ttk.Label(self, text='Địa chỉ:').grid(column=0, row=4, sticky=tkinter.W, pady=8)
        ttk.Label(self,text='Điểm trung bình:').grid(column=0, row=5, sticky=tkinter.W,pady=8)
        ttk.Label(self,text='Chuyên ngành:').grid(column=0, row=6, sticky=tkinter.W,pady=8)

        self.entry_cccd = ttk.Entry(self,textvariable=self.var_cccd)
        self.entry_cccd.grid(column=1,row=0,sticky=tkinter.EW,ipady=4,ipadx=4)

        self.entry_name = ttk.Entry(self,textvariable=self.var_name)
        self.entry_name.grid(column=1, row=1, sticky=tkinter.EW, ipady=4, ipadx=4)

        self.entry_birth = ttk.Entry(self,textvariable=self.var_birth)
        self.entry_birth.grid(column=1, row=2, sticky=tkinter.EW, ipady=4, ipadx=4)

        self.entry_email = ttk.Entry(self,textvariable=self.var_email)
        self.entry_email.grid(column=1, row=3, sticky=tkinter.EW, ipady=4, ipadx=4)

        self.entry_address = ttk.Entry(self, textvariable=self.var_address)
        self.entry_address.grid(column=1, row=4, sticky=tkinter.EW, ipady=4, ipadx=4)

        self.entry_gpa = ttk.Entry(self,textvariable=self.var_gpa)
        self.entry_gpa.grid(column=1, row=5, sticky=tkinter.EW, ipady=4, ipadx=4)

        self.majors = ['Công nghệ thông tin.',
                         'Công nghệ sinh học.',
                         'Đa phương tiện.',
                         'Quản trị kinh doanh.',
                         'Điện tử viễn thông.',
                         'Quản trị nhân lực.']
        self.box_major = ttk.Combobox(self,textvariable=self.var_major,height=5,values=self.majors,state='readonly')
        self.box_major.grid(column=1,row=6,sticky=tkinter.EW,ipady=4, ipadx=4)

        self.btn_cancel = ttk.Button(self,text='Cancel',command=self.destroy)
        self.btn_cancel.grid(column=0,row=7,padx=4,pady=8,sticky=tkinter.W)

        self.btn_add = ttk.Button(self,text='Add',command = self.add_student)
        self.btn_add.grid(column=1, row=7, padx=4, pady=8,sticky=tkinter.E)

    def add_student(self):
        cccd = self.entry_cccd.get().strip()
        name = self.entry_name.get().strip()
        birth = self.entry_birth.get().strip()
        email = self.entry_email.get().strip()
        address = self.entry_address.get().strip()
        gpa = self.entry_gpa.get().strip()
        major = self.box_major.get().strip()
        if len(cccd) == 0:
            showinfo(message='Lỗi cccd không được để trống !')
        elif cccd.isdigit() is False:
            showinfo(message='CCCD phải là số')
        elif len(address) == 0:
            showinfo(message='Lỗi address không được để trống !')
        elif len(major) == 0:
            showinfo(message='Vui lòng chọn major')
        else:
            s = StudentController()
            student = s.add(cccd,name,birth,email,gpa,major,address)
            if student is not None:
                self.mastter.item_create_student_selected(student)
                showinfo('Completion', message='Add new student successfully!')