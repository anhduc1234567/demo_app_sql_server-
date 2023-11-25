
import tkinter
from tkinter import ttk

class StaticView(tkinter.Tk):
    def __init__(self,tuple):
        super().__init__()
        self.configure(padx=8,pady=8)
        self.add_table(tuple)
    def add_table(self,tuple):
        colum = ['c1','c2','c3','c4']
        self.table = ttk.Treeview(self,columns=colum,show='headings',height=10)
        self.table.grid(column=0,row = 0,sticky=tkinter.NSEW)

        self.table.heading('c1',text='STT')
        self.table.heading('c2',text='Mã môn học')
        self.table.heading('c3',text='Tên môn học')
        self.table.heading('c4',text='Số lượng đăng ký')

        self.table.column(0,width=150,anchor=tkinter.CENTER,stretch=tkinter.NO)
        self.table.column(1,width=150,anchor=tkinter.CENTER,stretch=tkinter.NO)
        self.table.column(2,width=250,stretch=tkinter.NO)
        self.table.column(3,width=150,anchor=tkinter.CENTER,stretch=tkinter.NO)

        for i in tuple:
            self.table.insert('',tkinter.END,values=i)
