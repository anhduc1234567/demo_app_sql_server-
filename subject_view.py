import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from  subject_controller import SubjectController
from addsubjectview import EditSubjectView
from database_connect import insert_subjects_to_db,delete_subject_from_db
from subject import Subject
def clear_treeview(treeview):
    for i in treeview.get_children():
        treeview.delete(i)
def subject_to_tuple(subject):
    return tuple([subject.subject_id,subject.name,subject.credit,subject.lesson,subject.category])
class SubjectView:
    def __init__(self,frame):
        self.frame = frame
        self.subjects = []
        self.entry_key = tkinter.StringVar()
        self.add_table()
        self.add_frame_search()
        self.add_sort()
        self.add_buttons()
    def add_table(self):

        column = ['c1','c2','c3','c4','c5']
        self.subject_table = ttk.Treeview(self.frame,columns=column,height=9,show='headings',selectmode='browse')
        self.subject_table.grid(column= 0,columnspan=2,row=0,sticky=tkinter.NSEW)

        style = ttk.Style()
        style.theme_use('alt')  # other theme can use: clam, classic, default
        style.configure('my.Treeview.Heading', font=('Calibri', 11, 'bold'),
                        background='#33CCFF', foreground='#ffffff')
        self.subject_table.configure(style='my.Treeview')

        self.subject_table.heading('c1',text='Mã môn học')
        self.subject_table.heading('c2', text='Tên môn học')
        self.subject_table.heading('c3', text='Số tín ')
        self.subject_table.heading('c4', text='Số tiết')
        self.subject_table.heading('c5', text='Loại môn học')


        self.subject_table.column(0,width=250,minwidth=250, stretch=False,anchor=tkinter.CENTER)
        self.subject_table.column(1, width=250,minwidth=250)
        self.subject_table.column(2, width=200,minwidth=200,anchor=tkinter.CENTER)
        self.subject_table.column(3, width=200,minwidth=200,anchor=tkinter.CENTER)
        self.subject_table.column(4, width=220,minwidth=220)
    def add_frame_search(self):
        self.frame_search = ttk.LabelFrame(self.frame,text='Tìm kiếm')
        self.frame_search.grid(column=0,row=1,sticky=tkinter.NSEW, pady=4, padx=4)
        self.frame_search.grid_columnconfigure(0,weight=1)
        self.frame_search.grid_columnconfigure(1,weight=1)

        lable_search_by = ttk.Label(self.frame_search, text='Tiêu chí tìm kiếm').grid(column=0, row=0, sticky=tkinter.N)
        lable_search_key = ttk.Label(self.frame_search, text='Từ khóa').grid(column=1, row=0, sticky=tkinter.N)

        self.entry = ttk.Entry(self.frame_search, textvariable=self.entry_key).grid(column=1, row=2, sticky=tkinter.N,
                                                                                    ipady=4)

        searches = ('Theo tên gần đúng.', 'Theo mã môn học.', 'Theo số tín chỉ.', 'Theo số tiết học', 'Theo loại môn học')
        self.combo_search = ttk.Combobox(self.frame_search, state='readonly', height=5, values=searches)
        self.combo_search.grid(column=0, row=2, sticky=tkinter.N, ipady=4)

        self.btn_search = ttk.Button(self.frame_search, text='Search',command=self.search_by_key)
        self.btn_search.grid(column=0, row=3, sticky=tkinter.N, pady=8,columnspan=2)
    def add_sort(self):
        self.frame_sort = ttk.LabelFrame(self.frame,text='Sắp xếp')
        self.sort_var = tkinter.IntVar(value=0)
        self.frame_sort = ttk.LabelFrame(self.frame, text='Sắp xếp')
        self.frame_sort.columnconfigure(0, weight=1, uniform='fred')
        self.frame_sort.columnconfigure(1, weight=1, uniform='fred')
        self.frame_sort.grid(row=1, column=1, sticky=tkinter.NSEW, pady=4, padx=4)
        # add radio button to this frame
        ttk.Radiobutton(self.frame_sort,text='Mã môn học tăng dần.',value=1,variable=self.sort_var,command=self.com_sort_by_id)\
        .grid(column=0,row=0,sticky=tkinter.W,pady=4,padx=16)

        ttk.Radiobutton(self.frame_sort, text='Tên môn học a-z.', value=2, variable=self.sort_var,command=self.com_sort_name) \
            .grid(column=1, row=0, sticky=tkinter.W, pady=4,padx=16)

        ttk.Radiobutton(self.frame_sort, text='Số tín chỉ giảm dần.', value=3, variable=self.sort_var,command=self.com_sort_by_credit) \
            .grid(column=0, row=1, sticky=tkinter.W, pady=4,padx=16)

        ttk.Radiobutton(self.frame_sort, text='Số tiết học tăng dần.', value=4, variable=self.sort_var,command=self.com_sort_by_lesson) \
            .grid(column=1, row=1, sticky=tkinter.W, pady=4,padx=16)

        ttk.Radiobutton(self.frame_sort, text='Loại môn học a-z.', value=5, variable=self.sort_var,command=self.com_sort_by_cate) \
            .grid(column=0, row=2, sticky=tkinter.W, pady=4,padx=16)

    def add_buttons(self):
        self.frame_btn = ttk.LabelFrame(self.frame,text='Các thao tác')
        self.frame_btn.grid(column=0,columnspan=3,row=2,sticky=tkinter.NSEW)
        self.frame_btn.grid_columnconfigure(0,weight=1)
        self.frame_btn.grid_columnconfigure(1,weight=1)
        self.frame_btn.grid_columnconfigure(2,weight=1)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Làm mới',command=self.load_subject)
        self.btn_fresh.grid(column=0,row=0,pady=8,ipady=8,ipadx=16)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Sửa môn học',command=self.edit_subject)
        self.btn_fresh.grid(column=1, row=0,pady=8,ipady=8,ipadx=16)

        self.btn_fresh = ttk.Button(self.frame_btn, text='Xóa bỏ',command=self.delete_item)
        self.btn_fresh.grid(column=2, row=0,pady=8,ipady=8,ipadx=16)

    def load_subject(self):
        self.subjects.clear()
        s = SubjectController()
        self.subjects = s.read_subject()
        self.show_subject_table()

    def show_subject_table(self):
        clear_treeview(self.subject_table)
        index = 1
        self.subject_table.selection_clear()
        for i in self.subjects:
            if index % 2 == 0:
                tag = 'even'
            else:
                tag = 'odd'
            self.subject_table.insert('', tkinter.END, values=subject_to_tuple(i), tags=(tag,))
            index += 1

    def delete_item(self):
        item = self.subject_table.selection()
        s = SubjectController()
        if len(item) == 0:
            showinfo(message='Lỗi danh sách rỗng')
        else:
            id = self.subject_table.set(item[0],column='c1')
            for i in self.subjects:
                if i.subject_id == int(id):
                    self.subjects.remove(i)
            if len(item) == 0:
                showinfo(message='Lỗi danh sách rỗng')
            else:
                ask = askyesno(message='Bạn có chắc chắn muốn xóa ?')
                if ask:
                    for i in item:
                        self.subject_table.delete(i)
                    showinfo(message='Xóa thành công')
                    delete_subject_from_db(id)
    def com_sort_by_id(self):
        s = SubjectController()
        s.sort_by_id_sub(self.subjects)
        self.show_subject_table()
    def com_sort_name(self):
        s = SubjectController()
        s.sort_by_name(self.subjects)
        self.show_subject_table()
    def com_sort_by_credit(self):
        s = SubjectController()
        s.sort_by_credit(self.subjects)
        self.show_subject_table()
    def com_sort_by_lesson(self):
        s = SubjectController()
        s.sort_by_lesson(self.subjects)
        self.show_subject_table()
    def com_sort_by_cate(self):
        s = SubjectController()
        s.sort_by_category(self.subjects)
        self.show_subject_table()

    def search_by_key(self):
        key = self.entry_key.get()
        s = SubjectController()
        type = self.combo_search.get()
        searches = (
        'Theo tên gần đúng.', 'Theo mã môn học.', 'Theo số tín chỉ.', 'Theo số tiết học', 'Theo loại môn học')
        if len(type) == 0:
            showinfo(message='Vui lòng chọn tiêu chí tìm kiếm')
        elif len(key) == 0:
            showinfo(message='Lỗi key không được rỗng')
        else:
            if type == 'Theo tên gần đúng.':
                self.subjects = s.search_by_name(self.subjects,key)
                self.show_subject_table()
            elif type == 'Theo mã môn học.':
                if key.isdigit() is True and int(key) > 1000:
                     self.subjects = s.search_by_id(self.subjects,int(key))
                     self.show_subject_table()
                else:
                    showinfo(message='Key phải là số nguyên và lớn hơn 1000')
            elif type == 'Theo số tín chỉ.':
                if key.isdigit() is True and 2 <= int(key) <= 15:
                    self.subjects = s.search_by_credit(self.subjects,int(key))
                    self.show_subject_table()
                else:
                    showinfo(message='Key phải là số nguyên và trong đoạn 2 - 15')
            elif type == 'Theo số tiết học':
                if key.isdigit() is True and 1 <= int(key) <= 54:
                    self.subjects = s.search_by_lesson(self.subjects, int(key))
                    self.show_subject_table()
                else:
                    showinfo(message='Key phải là số nguyên và trong đoạn 1 - 54')
    def add_new_subject(self,subject):
        self.subjects.append(subject)
        s = SubjectController()
        # s.write_subject(self.subjects)
        insert_subjects_to_db([subject.subject_id,subject.name,subject.credit,subject.lesson,subject.category])
        self.show_subject_table()

    def edit_subject(self):
        item = self.subject_table.selection()
        if len(item) == 0:
            showinfo(message='Lỗi danh sách rỗng')
        else:
            app = EditSubjectView(self.subject_table,item,self.subjects)
            app.mainloop()


