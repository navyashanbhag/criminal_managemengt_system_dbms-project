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


class Stations:
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.title_space = ""
        self.root.title(102 * self.title_space + "Station info")
        self.root.geometry("796x572")
        self.root.resizable(width=False, height=False)

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
        # ===============================================================================================
        self.station_name= StringVar()
        self.station_incharge= StringVar()
        self.no_of_cells = StringVar()

        self.label_title = Label(self.TitleFrame, font=('arial', 40, 'bold'), text="Station Info", bd=7)
        self.label_title.grid(row=0, column=0, padx=132)

        self.label_station_name = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Station_name", bd=7)
        self.label_station_name.grid(row=0, column=0, sticky=W, padx=5)
        self.entry_station_name = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                        textvariable=self.station_name)
        self.entry_station_name.grid(row=0, column=1, sticky=W, padx=5)

        self.label_station_in_charge = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="Station_incharge", bd=7)
        self.label_station_in_charge.grid(row=1, column=0, sticky=W, padx=5)
        self.entry_station_in_charge = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44,
                                             justify='left',
                                             textvariable=self.station_incharge)
        self.entry_station_in_charge.grid(row=1, column=1, sticky=W, padx=5)

        self.label_cells = Label(self.LeftFrame1, font=('arial', 12, 'bold'), text="no_of_cells", bd=7)
        self.label_cells.grid(row=2, column=0, sticky=W, padx=5)
        self.entry_cells = Entry(self.LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                 textvariable=self.no_of_cells)
        self.entry_cells.grid(row=2, column=1, sticky=W, padx=5)

        # ============================================Tables=====================================================

        scroll_x = Scrollbar(self.LeftFrame, orient=VERTICAL)
        self.station_info = ttk.Treeview(self.LeftFrame, height=12,
                                         columns=("station_name", "station_incharge", "no_of_cells"),
                                         yscrollcommand=scroll_x.set)

        scroll_x.pack(side=RIGHT, fill=Y)

        self.station_info.heading("station_name", text="station_name")
        self.station_info.heading("station_incharge", text="station_incharge")
        self.station_info.heading("no_of_cells", text="no_of_cells")

        self.station_info['show'] = 'headings'

        self.station_info.column("station_name", width=70)
        self.station_info.column("station_incharge", width=100)
        self.station_info.column("no_of_cells", width=100)

        self.station_info.pack(fill=BOTH, expand=1)
        # DisplayData()
        self.station_info.bind("<ButtonRelease-1>", self.get_station_info)

        # ====================================================================================================

        self.btnAddNew = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="AddNew", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.add_station).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=self.display_station).grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.update_stations).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=self.delete_stations).grid(row=3, column=0, padx=1)

        self.btnReset = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=8,
                               height=2, command=self.station_reset).grid(row=4, column=0, padx=1)
        self.btnExit = Button(self.RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=8,
                              height=2, command=self.i_exit).grid(row=5, column=0, padx=1)

    def i_exit(self):
        i_exit = tkinter.messagebox.askyesno("MYSQL connection", "confirm if you want to exit")
        if i_exit > 0:
            self.root.destroy()
            return

    def station_reset(self):
        self.entry_station_name.delete(0, END)
        self.entry_station_in_charge.delete(0, END)
        self.entry_cells.delete(0, END)

    def add_station(self):
        if self.station_name.get() == "" or self.station_incharge.get() == "" or self.no_of_cells.get() == "":
            tkinter.messagebox.showerror("Mysql connection", "enter correct details")
        else:
            cur.execute(
                "insert into criminal.station_info values(%s,%s,%s)",
                (self.station_name.get(), self.station_incharge.get(), self.no_of_cells.get())
            )
            sqlCon.commit()
            self.display_station()
            tkinter.messagebox.showinfo("Mysql connection", "Successfully inserted")

    def display_station(self):
        cur.execute("select * from criminal.station_info")
        result = cur.fetchall()
        if len(result) != 0:
            for i in self.station_info.get_children():
                self.station_info.delete(i)
            # self.station_info.delete(*self.station_info.get_children())
            for row in result:
                self.station_info.insert('', END, values=row)
        sqlCon.commit()

    def get_station_info(self, event):
        print(event)
        view_info = self.station_info.focus()
        learner_data = self.station_info.item(view_info)
        row = learner_data['values']
        self.station_name.set(row[0])
        self.station_incharge.set(row[1])
        self.no_of_cells.set(row[2])

    def delete_stations(self):
        cur.execute("delete from criminal.station_info where station_name='{}'".format(self.station_name.get()))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Deletion", "Successfully deleted")
        self.display_station()
        self.station_reset()

    def update_stations(self):
        cur.execute(
            "update criminal.station_info set station_incharge=%s,no_of_cells=%s where station_name=%s", (
                self.station_incharge.get(),
                self.no_of_cells.get(),
                self.station_name.get()
            ))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Update", "Successfully updated")
        self.display_station()


if __name__ == '__main__':
    root = Tk()
    application = Stations(root)
    root.mainloop()
