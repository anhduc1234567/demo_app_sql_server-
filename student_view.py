import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from editgpaview import EditGpaView
from student_controller import StudentController
from exception import *
import matplotlib.pyplot as plt
import numpy as np
from database_connect import insert_person_to_db,insert_students_to_db,delete_person_from_db
def clear_treeview(treeview):
    for i in treeview.get_children():
        treeview.delete(i)
def student_to_tuple(students):
    return ([students.id,students.name,students.birth,students.student_id,students.email,students.address,students.gpa,students.major])
class StudentView:
    def __init__(self,frame):
        # super().__init__()
        self.frame = frame
        self.students = []
        self.controller = StudentController()
        self.entry_key = tkinter.StringVar()
        self.create_student_table()
        self.add_search()
        self.add_sort()
        self.add_chart()
        self.add_buttons()

        # self.load_student()
    def create_student_table(self):
        column = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7','c8')
        self.student_table = ttk.Treeview(self.frame, columns=column, height=9, show='headings',
                                          selectmode='browse')
        self.student_table.grid(column=0, row=0, sticky=tkinter.NSEW, columnspan=3)

        style = ttk.Style()
        style.theme_use('alt')  # other theme can use: clam, classic, default
        style.configure('my.Treeview.Heading', font=('Calibri', 11, 'bold'),
                        background='#fa8ec8', foreground='#ffffff')
        self.student_table.configure(style='my.Treeview')

        self.student_table.tag_configure('odd', background='#f0f0f0')
        self.student_table.tag_configure('even', background='#ffffff')

        self.student_table.heading('c1', text='CCCD')
        self.student_table.heading('c2', text='Họ và tên')
        self.student_table.heading('c3', text='Ngày sinh')
        self.student_table.heading('c4', text='Mã sinh viên')
        self.student_table.heading('c5', text='Email')
        self.student_table.heading('c6', text='Địa chỉ')
        self.student_table.heading('c7', text='Điểm trung bình')
        self.student_table.heading('c8', text='Chuyên ngành')

        self.student_table.column(0, width=100, minwidth=100, stretch=False,anchor=tkinter.CENTER)
        self.student_table.column(1, width=150, minwidth=150)
        self.student_table.column(2, width=100, minwidth=100,anchor=tkinter.CENTER)
        self.student_table.column(3, width=120, minwidth=120,anchor=tkinter.CENTER)
        self.student_table.column(4, width=180, minwidth=180)
        self.student_table.column(5, width=200, minwidth=200)
        self.student_table.column(6, width=120, minwidth=120,anchor=tkinter.CENTER)
        self.student_table.column(7, width=150, minwidth=150,anchor=tkinter.CENTER)

    def add_search(self):
        self.frame_search = ttk.LabelFrame(self.frame,text='Tìm kiếm')
        self.frame_search.grid(column=0,row=1,sticky=tkinter.NSEW,padx=4,pady=4)
        self.frame_search.grid_columnconfigure(0,weight=1)
        self.frame_search.grid_columnconfigure(1,weight=1)

        lable_search_by = ttk.Label(self.frame_search,text='Tiêu chí tìm kiếm').grid(column=0,row=0,sticky=tkinter.W)
        lable_search_key = ttk.Label(self.frame_search, text='Từ khóa').grid(column=1,row=0,sticky=tkinter.W)

        self.entry = ttk.Entry(self.frame_search,textvariable=self.entry_key).grid(column=1,row=2,sticky=tkinter.W,ipady=4)
        searches = ('Theo tên gần đúng.','Theo điểm.','Theo ngày sinh.','Theo tháng sinh','Theo năm sinh')
        self.combo_search = ttk.Combobox(self.frame_search,state='readonly',height = 5,values=searches)
        self.combo_search.grid(column=0,row=2,sticky=tkinter.W,ipady=4)

        self.btn_search = ttk.Button(self.frame_search,text='Search',command=self.com_search)
        self.btn_search.grid(column=1,row=3,sticky=tkinter.N,pady=8)

    def add_sort(self):
        self.frame_sort = ttk.LabelFrame(self.frame,text='Sắp xếp')
        self.sort_var = tkinter.IntVar(value=0)
        self.frame_sort = ttk.LabelFrame(self.frame, text='Sắp xếp')
        self.frame_sort.columnconfigure(0, weight=1, uniform='fred')
        self.frame_sort.columnconfigure(1, weight=1, uniform='fred')
        self.frame_sort.grid(row=1, column=1, sticky=tkinter.NSEW, pady=4, padx=4)
        # add radio button to this frame
        ttk.Radiobutton(self.frame_sort,text='Theo tên a - z',value=1,variable=self.sort_var,command=self.com_sort_by_name)\
        .grid(column=0,row=0,sticky=tkinter.W,pady=4)

        ttk.Radiobutton(self.frame_sort, text='Theo điểm trung bình', value=2, variable=self.sort_var,command=self.com_sort_by_gpa) \
            .grid(column=1, row=0, sticky=tkinter.W, pady=4)

        ttk.Radiobutton(self.frame_sort, text='Theo ngày sinh', value=3, variable=self.sort_var,command=self.com_sort_by_birth) \
            .grid(column=0, row=1, sticky=tkinter.W, pady=4)

        ttk.Radiobutton(self.frame_sort, text='Theo họ và tên', value=4, variable=self.sort_var,command=self.com_sort_by_name_first) \
            .grid(column=1, row=1, sticky=tkinter.W, pady=4)

    def add_chart(self):
        self.frame_chart = ttk.LabelFrame(self.frame,text='Biểu đồ')
        self.frame_chart.grid(column=2,row=1,sticky=tkinter.NSEW,padx=4,pady=4)
        self.frame_chart.grid_columnconfigure(0,weight=1)
        self.frame_chart.grid_columnconfigure(1,weight=1)

        self.frame_chart.grid_columnconfigure(0,weight=1)
        self.frame_chart.grid_rowconfigure(0,weight=1)

        self.btn_chart = ttk.Button(self.frame_chart,text='Vẽ biểu đồ',width=20,command=self.draw_chart).grid(column=0,row=0,columnspan=2)

    def add_buttons(self):
        self.frame_btn = ttk.LabelFrame(self.frame,text='Các thao tác')
        self.frame_btn.grid(column=0,columnspan=3,row=2,sticky=tkinter.NSEW)
        self.frame_btn.grid_columnconfigure(0,weight=1)
        self.frame_btn.grid_columnconfigure(1,weight=1)
        self.frame_btn.grid_columnconfigure(2,weight=1)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Làm mới',command=self.load_student)
        self.btn_fresh.grid(column=0,row=0,pady=8,ipady=8,ipadx=16)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Sửa điểm TB',command=self.edit_gpa)
        self.btn_fresh.grid(column=1, row=0,pady=8,ipady=8,ipadx=16)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Xóa bỏ',command=self.com_remove)
        self.btn_fresh.grid(column=2, row=0,pady=8,ipady=8,ipadx=16)

    def load_student(self):
        self.students.clear()
        s = StudentController()
        self.students = s.read_student()
        self.show_student_in_table()
    def show_student_in_table(self):
        clear_treeview(self.student_table)
        index = 1
        self.student_table.selection_clear()
        for student in self.students:
            if index % 2 == 0:
                tag = 'even'
            else:
                tag = 'odd'
            self.student_table.insert('', tkinter.END, values=student_to_tuple(student), tags=(tag,))
            index += 1
    def com_remove(self):
        s = StudentController()
        item = self.student_table.selection()
        if len(item) == 0 :
            showinfo(message='Lỗi danh sách rỗng')
        else:
            ask = askyesno(message='Bạn có chắc chắn muốn xóa ?')
            if ask :
                id = self.student_table.set(item[0], 'c4')
                for i in item:
                    self.student_table.delete(i)
                stu = None
                for i in self.students:
                    if i.student_id == id:
                        stu = i
                self.students.remove(stu)
                delete_person_from_db(stu.id)
                showinfo(message='Xóa thành công')
    def edit_gpa(self):
        item = self.student_table.selection()
        if len(item) == 0 :
            showinfo(message='Lỗi danh sách rỗng')
        else:
            edit = EditGpaView(self,self.student_table,item,self.students)
            edit.mainloop()



    def com_sort_by_name(self):
        s = StudentController()
        s.sort_by_name(self.students)
        self.show_student_in_table()

    def com_sort_by_gpa(self):
        s = StudentController()
        s.sort_by_gpa(self.students)
        self.show_student_in_table()

    def com_sort_by_birth(self):
        s = StudentController()
        s.sort_by_birth(self.students)
        self.show_student_in_table()

    def com_sort_by_name_first(self):
        s = StudentController()
        s.sort_by_name_first(self.students)
        self.show_student_in_table()

    def com_search(self):
        key = self.entry_key.get().strip()
        if key != '':
            s = StudentController()
            type_search = self.combo_search.get()
            if type_search == '':
                showinfo(message='Vui lòng chọn tiêu chí tìm kiếm')
            elif type_search == 'Theo tên gần đúng.':
                 self.students = s.search_by_name(self.students,key)
                 self.show_student_in_table()
            elif type_search == 'Theo điểm.':
                try:
                    if s.is_gpa_vaild(key):
                        self.students = s.search_by_gpa(self.students, key)
                        self.show_student_in_table()
                except GpaError as e:
                    showinfo(message=e.message)
            elif type_search == 'Theo ngày sinh.':
                if key.isdigit():
                    self.students = s.search_by_birth_day(self.students, key)
                    self.show_student_in_table()
                else:
                    showinfo(message='Ngày sinh lỗi ')
            elif type_search == 'Theo tháng sinh':
                if key.isdigit():
                    self.students = s.search_by_birth_month(self.students, key)
                    self.show_student_in_table()
                else:
                    showinfo(message='Tháng sinh lỗi ')
            elif type_search == 'Theo năm sinh':
                if key.isdigit():
                    self.students = s.search_by_birth_year(self.students, key)
                    self.show_student_in_table()
                else:
                    showinfo(message='Năm sinh lỗi ')
        else:
            showinfo(message='Lỗi key trống!')

    def item_create_student_selected(self,student):
        self.students.append(student)
        s = StudentController()
        # s.write_student(self.students)
        insert_person_to_db([student.id,student.name.first,student.name.mid,student.name.last,student.birth])
        insert_students_to_db([student.student_id,student.id,student.email,student.address,student.gpa,student.major])
        self.show_student_in_table()
    def draw_chart(self):
        yeu = 0
        trung_binh = 0
        kha = 0
        gioi = 0
        xuat_xac = 0
        if len(self.students) == 0:
            showinfo(message='Danh sách rỗng')
        else:
            for i in self.students:
                if float(i.gpa) < 2.0:
                      yeu += 1
                elif 2.0 <= float(i.gpa) < 2.6:
                      trung_binh += 1
                elif 2.6 <= float(i.gpa) < 3.2:
                      kha += 1
                elif 3.2 <= float(i.gpa) < 3.6:
                      gioi += 1
                else:
                      xuat_xac += 1
            list = [yeu,trung_binh,kha,gioi,xuat_xac]
            capacity = np.array(list)
            lable = ['Yếu','Trung Bình','Khá','Giỏi','Xuất xắc']
            explode = [0.2, 0.1, 0, 0, 0]
            plt.pie(capacity,labels=lable,shadow=True,startangle=45,explode=explode,
                    autopct='%1.2f%%',textprops={'color':'#ffffff'})
            plt.title('Biểu đồ học lực sinh viên')
            plt.legend(loc = 1 ,title = 'Học lực: ')
            plt.show()

