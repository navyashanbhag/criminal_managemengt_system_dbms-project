from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as mysql


sqlCon = mysql.connect(
            host="localhost",
            user="root",
            passwd="maravanthe2001",
            database="criminal",
            port="3306"
        )
cur = sqlCon.cursor()


class Police:
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.title_space = ""
        self.root.title(102 * self.title_space + "police_info")
        self.root.geometry("796x572")
        self.root.resizable(width=False, height=False)

        self.app_status = False

        self.main_frame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='cadet blue')
        self.main_frame.grid()

        self.title_frame = Frame(self.main_frame, bd=10, width=770, height=100, relief=RIDGE)
        self.title_frame.grid(row=0, column=0)
        self.top_frame3 = Frame(self.main_frame, bd=5, width=770, height=500, relief=RIDGE)
        self.top_frame3.grid(row=1, column=0)

        self.left_frame = Frame(self.top_frame3, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='cadet blue')
        self.left_frame.pack(side=LEFT)
        self.left_frame1 = Frame(self.left_frame, bd=5, width=600, height=180, padx=2, pady=12, relief=RIDGE)
        self.left_frame1.pack(side=TOP)

        self.right_frame1 = Frame(self.top_frame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg='cadet blue')
        self.right_frame1.pack(side=RIGHT)
        self.right_frame1a = Frame(self.right_frame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        self.right_frame1a.pack(side=TOP)
        # ===============================================================================================
        self.police_id = StringVar()
        self.police_name = StringVar()
        self.station_name = StringVar()

        # =========================================================================================

        self.label_title = Label(self.title_frame, font=('arial', 40, 'bold'), text="Police Info", bd=7)
        self.label_title.grid(row=0, column=0, padx=132)

        self.label_police_id = Label(self.left_frame1, font=('arial', 12, 'bold'), text="Police_id", bd=7)
        self.label_police_id.grid(row=0, column=0, sticky=W, padx=5)
        self.entry_police_id = Entry(self.left_frame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                     textvariable=self.police_id)
        self.entry_police_id.grid(row=0, column=1, sticky=W, padx=5)

        self.label_police_name = Label(self.left_frame1, font=('arial', 12, 'bold'), text="police_name", bd=7)
        self.label_police_name.grid(row=1, column=0, sticky=W, padx=5)
        self.entry_police_name = Entry(self.left_frame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                       textvariable=self.police_name)
        self.entry_police_name.grid(row=1, column=1, sticky=W, padx=5)

        self.label_station_name = Label(self.left_frame1, font=('arial', 12, 'bold'), text="station_name", bd=7)
        self.label_station_name.grid(row=2, column=0, sticky=W, padx=5)
        self.entry_station_name = Entry(self.left_frame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                        textvariable=self.station_name)
        self.entry_station_name.grid(row=2, column=1, sticky=W, padx=5)

        # ============================================Tables=====================================================

        self.scroll_x = Scrollbar(self.left_frame, orient=VERTICAL)
        self.police_info = ttk.Treeview(self.left_frame, height=12,
                                        columns=("police_id", "police_name", "station_name"),
                                        yscrollcommand=self.scroll_x.set)

        self.scroll_x.pack(side=RIGHT, fill=Y)

        self.police_info.heading("police_id", text="police_id")
        self.police_info.heading("police_name", text="police_name")
        self.police_info.heading("station_name", text="station_name")

        self.police_info['show'] = 'headings'

        self.police_info.column("police_id", width=70)
        self.police_info.column("police_name", width=100)
        self.police_info.column("station_name", width=100)

        self.police_info.pack(fill=BOTH, expand=1)
        # DisplayData()
        self.police_info.bind("<ButtonRelease-1>", self.get_police_info)

        # ====================================================================================================

        self.btnAddNew = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="AddPolice", bd=4, pady=1, padx=24,
                                width=8, height=2, command=self.add_police).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=self.display_police).grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8, height=2, command=self.update_police).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8, height=2, command=self.delete_police).grid(row=3, column=0, padx=1)

        self.btnReset = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=8, height=2, command=self.reset).grid(row=4, column=0, padx=1)
        self.btnExit = Button(self.right_frame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=8, height=2, command=self.exit_app).grid(row=5, column=0, padx=1)

    def exit_app(self):
        i_exit = tkinter.messagebox.askyesno("MYSQL connection", "confirm if you want to exit")
        if i_exit > 0:
            self.root.destroy()

    def reset(self):
        self.entry_police_id.delete(0, END)
        self.entry_police_name.delete(0, END)
        self.entry_station_name.delete(0, END)

    def add_police(self):
        try:
            if self.police_id.get() == "" or self.police_name.get() == "" or self.station_name.get() == "":
                tkinter.messagebox.showerror("Mysql connection", "enter correct details")
            else:
                cur.execute(
                    "insert into criminal.police_info values ('{}','{}','{}')".format(
                        self.police_id.get(), self.police_name.get(), self.station_name.get())
                )
                sqlCon.commit()
                tkinter.messagebox.showinfo("Mysql connection", "Successfully inserted")
                self.display_police()
        except mysql.IntegrityError:
            tkinter.messagebox.showwarning("Mysql connection", "Duplicate id Found")

    def display_police(self):
        cur.execute("select * from criminal.police_info")
        result = cur.fetchall()
        sqlCon.commit()
        if len(result) != 0:
            for i in self.police_info.get_children():
                self.police_info.delete(i)
            # self.police_info.delete(*self.police_info.get_children())
            for row in result:
                self.police_info.insert('', END, values=row)

    def get_police_info(self, event):
        print(event)
        view_info = self.police_info.focus()
        learner_data = self.police_info.item(view_info)
        row = learner_data['values']
        self.police_id.set(row[0])
        self.police_name.set(row[1])
        self.station_name.set(row[2])

    def delete_police(self):
        cur.execute("delete from criminal.police_info where police_id='{}'".format(self.police_id.get()))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Deletion", "Successfully deleted")
        self.display_police()
        self.reset()

    def update_police(self):
        cur.execute(
            "update criminal.police_info set police_name=%s,station_name=%s where police_id=%s", (
                self.police_name.get(),
                self.station_name.get(),
                self.police_id.get()
            ))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Update", "Successfully updated")
        self.display_police()


if __name__ == '__main__':
    try:
        root = Tk()
        application = Police(root)
        root.mainloop()
    except mysql.Error as e:
        print("Error : " + str(e))
