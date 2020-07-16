import tkinter as tk
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
        
    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        btn_open_dialog = tk.Button(toolbar, text='Ввести данные пациента', command=self.open_dialog, bg='#d7d8e0', bd=0,
        compound=tk.TOP)# image=self.add_img)
        
        btn_open_dialog.pack(side=tk.LEFT)
        self.tree = ttk.Treeview(self, columns=('number', 'surname', 'password_age', 'vascular_age'), height=15, show='headings')
        self.tree.column('number', width=30, anchor=tk.CENTER)
        self.tree.column('surname', width=305, anchor=tk.CENTER)
        self.tree.column('password_age', width=130, anchor=tk.CENTER)
        self.tree.column('vascular_age', width=130, anchor=tk.CENTER)
        self.tree.heading('number', text='№')
        self.tree.heading('password_age', text='Паспортный возраст')
        self.tree.heading('vascular_age', text='Сосудистый возраст')
        self.tree.heading('surname', text='ФИО')
        self.tree.pack()
    def records(self, surname, password_age, vascular_age):
        self.db.insert_data(surname, password_age, vascular_age)
        self.view_records()
            
    def view_records(self):
        self.db.c.execute('''SELECT * FROM patients_data_1''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
        
    def init_child(self):
        self.title('Ввести данные пациента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_name = tk.Label(self, text='ФИО пациента')
        label_name.place(x=50, y=10)
        label_password_age = tk.Label(self, text='Возраст:')
        label_password_age.place(x=50, y=60)
        label_vascular_age = tk.Label(self, text='Возраст:')
        label_vascular_age.place(x=50, y=110)
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x=200, y=10)
        self.entry_password_age = ttk.Entry(self)
        self.entry_password_age.place(x=200, y=60)
        self.entry_vascular_age = ttk.Entry(self)
        self.entry_vascular_age.place(x=200, y=110)
       # self.combobox = ttk.Combobox(self, values=[u'Паспортный', u'Сосудистый'])
       # self.combobox.current(0)
       # self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Ввести')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_surname.get(),self.entry_password_age.get(), self.entry_vascular_age.get()))

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('patients_data_1.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS patients_data_1 (id integer primary key, surname text, password_age real, vascular_age real)''')
        self.conn.commit()
    def insert_data(self, surname, password_age, vascular_age):
        self.c.execute('''INSERT INTO patients_data_1 (surname, password_age, vascular_age) VALUES (?, ?, ?)''',
                       (surname, password_age, vascular_age))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Диспансеризация")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()