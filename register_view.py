import re
import matplotlib.pyplot as plt
import  numpy as np
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from  static_view import StaticView
from register_controller import RegisterController
from database_connect import insert_register_to_db,delete_register_from_db
def clear_treeview(treeview):
    for i in treeview.get_children():
        treeview.delete(i)
def register_to_tuple(register):
    return tuple([register.register_id,register.subject.subject_id,
                  register.subject.name,register.student.student_id,
                  register.student.name,register.register_time])
class RegisterView:
    def __init__(self,frame,student_view,subject_view):
        super().__init__()
        self.frame = frame
        self.registers = []
        self.add_table_register()
        self.create_search_frame()
        self.creat_frame_sort()
        self.create_register_frame(student_view,subject_view)
        self.create_btn_frame(student_view,subject_view)

    def add_table_register(self):
        column = ['c1','c2','c3','c4','c5','c6']
        self.table_register = ttk.Treeview(self.frame,columns=column,show='headings',height=9,selectmode='browse')
        self.table_register.grid(column=0,row=0,columnspan=3,sticky=tkinter.NSEW)

        style = ttk.Style()
        style.theme_use('alt')  # other theme can use: clam, classic, default
        style.configure('my.Treeview.Heading', font=('Calibri', 11, 'bold'),
                        background='#33CCFF', foreground='#ffffff')
        self.table_register.configure(style='my.Treeview')

        self.table_register.heading('c1',text='Mã đăng ký')
        self.table_register.heading('c2',text='Mã môn học')
        self.table_register.heading('c3',text='Tên môn học')
        self.table_register.heading('c4',text='Mã sinh viên')
        self.table_register.heading('c5',text='Họ và tên')
        self.table_register.heading('c6',text='Thời gian')

        self.table_register.column(0,stretch=tkinter.NO,width=150,minwidth=150,anchor=tkinter.CENTER)
        self.table_register.column(1,stretch=tkinter.NO,width=150,minwidth=150,anchor=tkinter.CENTER)
        self.table_register.column(2,stretch=tkinter.NO,width=250,minwidth=250)
        self.table_register.column(3,stretch=tkinter.NO,width=150,minwidth=150,anchor=tkinter.CENTER)
        self.table_register.column(4,stretch=tkinter.NO,width=200,minwidth=200)
        self.table_register.column(5,stretch=tkinter.NO,width=250,minwidth=250,anchor=tkinter.CENTER)

    def create_search_frame(self):
        self.search_var = tkinter.StringVar()
        frm_search = ttk.LabelFrame(self.frame, text='Tìm kiếm')
        # config set all columns have same width space
        frm_search.columnconfigure(0, weight=1, uniform='fred')
        frm_search.columnconfigure(1, weight=1, uniform='fred')
        frm_search.grid(row=1, column=0, sticky=tkinter.NSEW, pady=4, padx=4)
        # add combobox
        ttk.Label(frm_search, text='Tiêu chí tìm kiếm:'). \
            grid(row=0, column=0, sticky=tkinter.W, pady=4, padx=4)
        type = ['Theo mã sinh viên','Theo mã môn học']
        self.combo_search =  ttk.Combobox(frm_search,   textvariable=self.search_var,values=type)
        self.combo_search.grid(row=1, column=0, padx=4, pady=4, sticky=tkinter.W,
                 ipady=4, ipadx=4)
        # add search part
        ttk.Label(frm_search, text='Từ khóa:'). \
            grid(row=0, column=1, sticky=tkinter.W, padx=4, pady=4)
        self.search_entry = ttk.Entry(frm_search)
        self.search_entry.grid(row=1, column=1, sticky=tkinter.EW, padx=4, pady=4,
                               ipadx=4, ipady=4)

        self.btn_search = ttk.Button(frm_search, text='Tìm kiếm', width=15,command=self.search_by_key)
        self.btn_search.grid(row=2, column=1, padx=4, pady=4)

    def creat_frame_sort(self):
        self.sort_var = tkinter.IntVar(value=0)
        frm_sort= ttk.LabelFrame(self.frame, text='Sắp xếp')
        # config set all columns have same width space
        frm_sort.columnconfigure(0, weight=1, uniform='fred')
        frm_sort.columnconfigure(1, weight=1, uniform='fred')
        frm_sort.grid(row=1, column=1, sticky=tkinter.NSEW, pady=4, padx=4)

        ttk.Radiobutton(frm_sort, text='Thứ tự đăng ký sớm-muộn', value=1,
                        variable=self.sort_var,command=self.sort_by_time). \
            grid(row=0, column=0, pady=4, padx=4, sticky=tkinter.W)
        ttk.Radiobutton(frm_sort, text='Thứ tự đăng ký muộn-sớm',
                        value=2, variable=self.sort_var,command=self.sort_by_time_d). \
            grid(row=1, column=0, pady=4, padx=4, sticky=tkinter.W)
        ttk.Radiobutton(frm_sort, text='Theo mã môn học tăng dần',
                        value=3, variable=self.sort_var,command=self.sort_by_id_sub). \
            grid(row=0, column=1, pady=4, padx=4, sticky=tkinter.W)
        ttk.Radiobutton(frm_sort, text='Theo mã sinh viên tăng dần',
                        value=4, variable=self.sort_var,command=self.sort_by_id_student). \
            grid(row=1, column=1, pady=4, padx=4, sticky=tkinter.W)

    def create_register_frame(self,student_view,subject_view):
        frm_register = ttk.LabelFrame(self.frame,text='Đăng ký môn học')
        frm_register.grid(column=2,row=1,sticky=tkinter.NSEW,padx=4,pady=4)
        frm_register.grid_columnconfigure(0,weight=1,uniform='fred')
        frm_register.grid_columnconfigure(1,weight=1,uniform='fred')

        frm_register.rowconfigure(0, weight=1, uniform='fred')
        frm_register.rowconfigure(1, weight=1, uniform='fred')
        frm_register.rowconfigure(2, weight=1, uniform='fred')

        ttk.Label(frm_register,text='Mã sinh viên').grid(column = 0 ,row=0,pady=4,padx=16)
        ttk.Label(frm_register,text='Mã môn học').grid(column = 0,row=1,padx=16,pady=4)

        self.entry_id_student = ttk.Entry(frm_register)
        self.entry_id_student.grid(column=1,row=0,padx=16,pady=4)

        self.entry_id_sub = ttk.Entry(frm_register)
        self.entry_id_sub.grid(column=1,row=1,padx=16,pady=4)

        self.btn_ok = ttk.Button(frm_register,text='REGISTER',command=lambda : self.register_subject(student_view,subject_view))
        self.btn_ok.grid(column=1,row=2,pady=4,padx=4)

    def create_btn_frame(self,students,subjects):
        self.frm_btn = ttk.LabelFrame(self.frame,text='Các thao tác')
        self.frm_btn.grid(column=0,row=2,columnspan=3,sticky=tkinter.NSEW)
        self.frm_btn.grid_columnconfigure(0,weight=1)
        self.frm_btn.grid_columnconfigure(1,weight=1)
        self.frm_btn.grid_columnconfigure(2,weight=1)
        self.frm_btn.grid_columnconfigure(3,weight=1)


        self.btn_load = ttk.Button(self.frm_btn,text='Làm mới',command=lambda :self.load_register(students,subjects))
        self.btn_load.grid(column=0,row=0,pady=8,padx=8,ipady=8,ipadx=16)

        self.btn_static = ttk.Button(self.frm_btn, text='Thống kê',command=self.static)
        self.btn_static.grid(column=1, row=0,pady=8,padx=8,ipady=8,ipadx=16)

        self.btn_draw = ttk.Button(self.frm_btn, text='Vẽ biểu đồ',command=self.draw_chart)
        self.btn_draw.grid(column=2, row=0,pady=8,padx=8,ipady=8,ipadx=16)

        self.btn_delete = ttk.Button(self.frm_btn, text='Xoá',command=self.delete_item)
        self.btn_delete.grid(column=3, row=0,pady=8,padx=8,ipady=8,ipadx=16)

    def load_register(self,students,subject):
        self.registers.clear()
        s = RegisterController()
        if len(students.students) == 0 or len(subject.subjects) == 0:
            showinfo(message='Lỗi danh sách rỗng')
        else:
            self.registers = s.read_data(students.students,subject.subjects)
            self.show_table_register()

    def show_table_register(self):
        clear_treeview(self.table_register)
        index = 1
        self.table_register.selection_clear()
        for i in self.registers:
            if index % 2 == 0:
                tag = 'even'
            else:
                tag = 'odd'
            self.table_register.insert('', tkinter.END, values=register_to_tuple(i), tags=(tag,))
            index += 1

    def sort_by_time(self):
        s = RegisterController()
        s.sort_by_time(self.registers)
        self.show_table_register()

    def sort_by_time_d(self):
        s = RegisterController()
        s.sort_by_time_d(self.registers)
        self.show_table_register()

    def sort_by_id_sub(self):
        s = RegisterController()
        s.sort_by_id_sub(self.registers)
        self.show_table_register()

    def sort_by_id_student(self):
        s = RegisterController()
        s.sort_by_id_student(self.registers)
        self.show_table_register()

    def search_by_key(self):
        type = self.combo_search.get()
        key = self.search_entry.get()
        s = RegisterController()
        if len(type) == 0 or len(key) == 0:
            showinfo(message='Lỗi key hoặc tiêu chí tìm kiếm không được rỗng')
        else:
            if type == 'Theo mã sinh viên':
                pattern = '^SV\\d{4}$'
                if re.match(pattern,key):
                    self.registers = s.search_by_id_student(self.registers,key)
                    self.show_table_register()
                else:
                    showinfo(message='Lỗi mã sinh vien không hợp lệ')
            else:
                if key.isdigit() is True and int(key) > 1000:
                    self.registers = s.search_by_id_subject(self.registers,int(key))
                    self.show_table_register()
                else:
                    showinfo(message='Lỗi mã môn học phải là số nguyên lớn hơn 1000')
    def check_register_exist(self,register):
        for i in self.registers:
            if i.student.student_id == register.student.student_id and i.subject.subject_id == register.subject.subject_id:
                return True
        return False
    def register_subject(self,students,subjects):
        s = RegisterController()
        id_student = self.entry_id_student.get()
        id_subject = self.entry_id_sub.get()
        pattern = '^SV\\d{4}$'
        if re.match(pattern, id_student) and id_subject.isdigit() and int(id_subject) > 1000:
            register = s.add(students.students,subjects.subjects,int(id_subject),id_student)
            if register is not None:
                if self.check_register_exist(register):
                    showinfo(message='Sinh viên đã đăng ký môn học trước đó')
                else:
                    self.registers.append(register)
                    self.show_table_register()
                    insert_register_to_db([register.register_id,register.subject.subject_id,register.student.student_id,register.register_time])
                    showinfo(message='Đăng ký thành công')
            else:
                showinfo(message='Sinh viên hoặc môn học không tồn tại')
        else:
            showinfo(message='Mã sinh viên hoặc mã môn học không hợp lệ')

    def delete_item(self):
        item = self.table_register.selection()
        if len(item) == 0:
            showinfo(message='Lỗi danh sách rỗng')
        else:
            id = self.table_register.set(item[0], column='c1')
            for i in self.registers:
                if i.register_id == int(id):
                    self.registers.remove(i)

            if len(item) == 0:
                showinfo(message='Lỗi danh sách rỗng')
            else:
                ask = askyesno(message='Bạn có chắc chắn muốn xóa ?')
                if ask:
                    for i in item:
                        self.table_register.delete(i)
                    showinfo(message='Xóa thành công')
                    delete_register_from_db(id)


    def create_dic(self):
        dic = {}
        for i in self.registers:
            if i.subject.subject_id in dic:
                dic[i.subject.subject_id] += 1
            else:
                dic[i.subject.subject_id] = 1
        return dic
    def getname(self,id):
        for i in self.registers:
            if i.subject.subject_id == id:
                return i.subject.name

    def static(self):
        list = []
        dic = self.create_dic()
        if len(dic) == 0 :
            showinfo(message='Lỗi danh sach rỗng')
        else:
            stt = 1
            for i in dic.keys():
                list.append(tuple([stt,i,self.getname(i),dic[i]]))
                stt += 1
            stat = StaticView(list)
            stat.mainloop()
    def draw_chart(self):
        dic = self.create_dic()
        if len(dic) == 0 :
            showinfo(message='Lỗi danh sach rỗng')
        else:
            num_subjects = []
            lable = []
            for i in dic.keys():
                num_subjects.append(dic[i])
                lable.append(i)

            subjects = np.array(num_subjects)
            plt.pie(subjects, labels=lable, shadow=True, startangle=45,
                    autopct='%1.2f%%', textprops={'color': '#ffffff'})
            plt.title('Biểu đồ phân bố đăng ký môn học')
            plt.legend(loc = 1 ,title = 'Môn học: ')
            plt.show()


