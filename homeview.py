from tkinter import ttk
from tkinter import Menu
import tkinter
from student_view import StudentView
from CreateStudent import AddStudentView
from subject_view import SubjectView
from addsubjectview import AddSubjectView
from register_view import RegisterView
class HomeView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.menubar = Menu()
        self.resizable(False,False)
        self.configure(menu=self.menubar)
        self.configure(pady=8,padx=8)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.add_widgets()
        self.students = []
        self.create_student_view()
        # self.add_student_view = AddStudentView()

    def add_widgets(self):
        self.menu_file = Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label='File',menu=self.menu_file)

        self.menu_file.add_command(label='Create new student',command=self.create_new_student)
        self.menu_file.add_command(label='Create new subject',command=self.create_new_subject)

        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', command=self.destroy)

        self.student_note = ttk.Notebook()
        self.student_note.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.frame_student = ttk.Frame(self.student_note)
        self.frame_student.grid(column=0,row=0)
        self.student_note.add(self.frame_student,text='StudentManagerment')
        self.frame_student.grid_columnconfigure(0,weight=1)
        self.frame_student.grid_columnconfigure(1, weight=1)
        self.frame_student.grid_columnconfigure(2, weight=1)

        self.frame_subjetc = ttk.Frame(self.student_note)
        self.frame_subjetc.grid(column=0,row=0)
        self.frame_subjetc.grid_columnconfigure(0,weight=1)
        self.frame_subjetc.grid_columnconfigure(1,weight=1)
        self.student_note.add(self.frame_subjetc, text='SubjectManagerment')

        self.frame_register = ttk.Frame(self.student_note)
        self.frame_register.grid(column=0, row=0)
        self.frame_register.grid_columnconfigure(0, weight=1)
        self.frame_register.grid_columnconfigure(1, weight=1)
        self.frame_register.grid_columnconfigure(2, weight=1)
        self.student_note.add(self.frame_register, text='RegisterManagerment')
    def create_student_view(self):
        self.student_view = StudentView(self.frame_student)
        self.subject_view = SubjectView(self.frame_subjetc)
        self.register_view = RegisterView(self.frame_register,self.student_view,self.subject_view)
    def create_new_student(self):
        main = AddStudentView(self.student_view)
        main.attributes('-topmost', True)
        main.mainloop()
    def create_new_subject(self):
        main = AddSubjectView(self.subject_view)
        main.attributes('-topmost', True)
        main.mainloop()


if __name__ == '__main__':
    app = HomeView()
    app.mainloop()