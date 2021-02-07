import os
import tkinter.messagebox
from police import *
from stations import *
import mysql.connector as mysql

sqlCon = mysql.connect(
    host="localhost",
    user="root",
    passwd="maravanthe2001",
    database="criminal",
    port="3306"
)
cur = sqlCon.cursor()


# noinspection PyAttributeOutsideInit
class ConnectorDb:
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.init_size()
        self.init_frame()
        self.init_prop()

    def init_frame(self):
        self.MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='cadet blue')
        self.MainFrame.grid()

        self.TitleFrame = Frame(self.MainFrame, bd=10, width=770, height=100, relief=RIDGE)
        self.TitleFrame.grid(row=0, column=0)
        self.TopFrame3 = Frame(self.MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        self.TopFrame3.grid(row=1, column=0)

        self.LeftFrame = Frame(self.TopFrame3, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='cadet blue')
        self.LeftFrame.pack(side=LEFT)
        self.LeftFrame1 = Frame(self.LeftFrame, bd=5, width=600, height=180, padx=2, pady=12, relief=RIDGE)
        self.LeftFrame1.pack(side=TOP)

        self.RightFrame1 = Frame(self.TopFrame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg='cadet blue')
        self.RightFrame1.pack(side=RIGHT)
        self.RightFrame1a = Frame(self.RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        self.RightFrame1a.pack(side=TOP)

    def init_prop(self):
        self.criminal_id = StringVar()
        self.criminal_name = StringVar()
        self.crime_name = StringVar()
        self.place = StringVar()
        self.police_id = StringVar()

        self.label_title = Label(self.TitleFrame, font=('arial', 40, 'bold'), text="Criminal database", bd=7)
        self.label_title.grid(row=0, column=0, padx=132)

        self.label_criminal_id = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Criminal_Id", bd=7)
        self.label_criminal_id.grid(row=0, column=0, sticky=W, padx=5)
        self.entry_criminal_id = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entry_criminal_id.grid(row=0, column=1, sticky=W, padx=5)

        self.label_criminal_name = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Criminal_Name", bd=7)
        self.label_criminal_name.grid(row=1, column=0, sticky=W, padx=5)
        self.entry_criminal_name = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                         textvariable=self.criminal_name)
        self.entry_criminal_name.grid(row=1, column=1, sticky=W, padx=5)

        self.label_crime_name = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Crime_Name", bd=7)
        self.label_crime_name.grid(row=2, column=0, sticky=W, padx=5)
        self.entry_crime_name = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=self.crime_name)
        self.entry_crime_name.grid(row=2, column=1, sticky=W, padx=5)

        self.label_place = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Place", bd=7)
        self.label_place.grid(row=3, column=0, sticky=W, padx=5)
        self.entry_place = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                 textvariable=self.place)
        self.entry_place.grid(row=3, column=1)

        self.label_police_id = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Police_id", bd=7)
        self.label_police_id.grid(row=4, column=0, sticky=W, padx=5)
        self.entry_police_id = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                     textvariable=self.police_id)
        self.entry_police_id.grid(row=4, column=1)

        # ============================================Tables=====================================================

        self.scroll_x = Scrollbar(self.LeftFrame, orient=VERTICAL)
        self.criminal_info = ttk.Treeview(self.LeftFrame, height=12,
                                          columns=("criminal_id", "criminal_name", "crime_name", "place", "police_id"),
                                          yscrollcommand=self.scroll_x.set)

        self.scroll_x.pack(side=RIGHT, fill=Y)

        self.criminal_info.heading("criminal_id", text="Criminal_Id")
        self.criminal_info.heading("criminal_name", text="Criminal_Name")
        self.criminal_info.heading("crime_name", text="Crime_name")
        self.criminal_info.heading("place", text="Place")
        self.criminal_info.heading("police_id", text="Police_Id")

        self.criminal_info['show'] = 'headings'

        self.criminal_info.column("criminal_id", width=70)
        self.criminal_info.column("criminal_name", width=100)
        self.criminal_info.column("crime_name", width=100)
        self.criminal_info.column("place", width=100)
        self.criminal_info.column("police_id", width=70)

        self.criminal_info.pack(fill=BOTH, expand=1)
        # DisplayData()
        self.criminal_info.bind("<ButtonRelease-1>", self.get_criminal_info)

        # ====================================================================================================

        self.btnAddNew = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="AddNew", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.add_data).grid(row=0, column=0, padx=1)

        self.btnDisplay = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=self.display_data).grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.update).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.delete_db).grid(row=3, column=0, padx=1)

        self.btnSearch = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.search).grid(row=4, column=0, padx=1)

        self.btnReset = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=8,
                               height=2, command=self.reset_data).grid(row=5, column=0, padx=1)

        self.btnPolice = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Police Info", bd=4, pady=1,
                                padx=24, width=8,
                                height=2, command=self.police_info).grid(row=6, column=0, padx=1)

        self.btnStation = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Station Info", bd=4, pady=1,
                                 padx=24, width=8,
                                 height=2, command=self.station_info).grid(row=7, column=0, padx=1)

        self.btnExit = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=8,
                              height=2, command=self.exit_criminal_app).grid(row=8, column=0, padx=1)

    def init_size(self):
        self.title_space = ""
        self.root.title(102 * self.title_space + "MYSQL connector")
        self.root.geometry("810x780+200+0")
        # self.root.resizable(width=False, height=False)

    def exit_criminal_app(self):
        i_exit = tkinter.messagebox.askyesno("MYSQL connection", "confirm if you want to exit")
        if i_exit > 0:
            self.root.destroy()
            return

    def reset_data(self):
        self.entry_criminal_id.delete(0, END)
        self.entry_criminal_name.delete(0, END)
        self.entry_crime_name.delete(0, END)
        self.entry_place.delete(0, END)
        self.entry_police_id.delete(0, END)

    def add_data(self):
        try:
            if self.entry_criminal_id.get() == "" or self.entry_criminal_name.get() == "" or \
                    self.entry_crime_name.get() == "" or self.entry_place.get() == "" or \
                    self.entry_police_id.get() == "":
                tkinter.messagebox.showerror("Mysql connection", "enter correct details")
            else:
                cur.execute(
                    "insert into criminal.criminal_info values ('{}','{}','{}','{}','{}')".format(
                        self.entry_criminal_id.get(), self.entry_criminal_name.get(), self.entry_crime_name.get(),
                        self.entry_place.get(), self.entry_police_id.get())
                )
                sqlCon.commit()
                tkinter.messagebox.showinfo("Mysql connection", "Successfully inserted")
                self.display_data()
        except mysql.IntegrityError:
            tkinter.messagebox.showerror("Mysql connection", "Duplicate Id Found")

    def display_data(self):
        cur.execute("select * from criminal_info")
        result = cur.fetchall()
        if len(result) != 0:
            for i in self.criminal_info.get_children():
                self.criminal_info.delete(i)
            for row in result:
                self.criminal_info.insert('', END, values=row)
        sqlCon.commit()

    def get_criminal_info(self, event):
        print(event)
        view_info = self.criminal_info.focus()
        learner_data = self.criminal_info.item(view_info)
        row = learner_data['values']
        self.criminal_id.set(row[0])
        self.criminal_name.set(row[1])
        self.crime_name.set(row[2])
        self.place.set(row[3])
        self.police_id.set(row[4])

    def delete_db(self):
        cur.execute("delete from criminal_info where criminal_id='{}'".format(self.criminal_id.get()))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Deletion", "Successfully deleted")
        self.display_data()
        self.reset_data()

    def update(self):
        cur.execute(
            "update criminal_info set criminal_name=%s,crime_name=%s,place=%s,police_id=%s where criminal_id=%s", (
                self.criminal_name.get(),
                self.crime_name.get(),
                self.place.get(),
                self.police_id.get(),
                self.criminal_id.get()
            ))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Update", "Successfully updated")
        self.display_data()

    def search(self):
        cur.execute("select * from criminal.criminal_info where criminal_id='{}'".format(self.entry_criminal_id.get()))
        row = cur.fetchall()
        print(row)
        sqlCon.commit()
        if len(row) != 0:
            self.criminal_name.set(row[0][1])
            self.crime_name.set(row[0][2])
            self.place.set(row[0][3])
            self.police_id.set(row[0][4])
        else:
            tkinter.messagebox.showinfo("Mysql connection", "No record found")
            self.reset_data()
        # =========================================================================================

    @staticmethod
    def station_info():
        os.system("python stations.py")

    @staticmethod
    def police_info():
        os.system("python police.py")


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDb(root)
    root.mainloop()
