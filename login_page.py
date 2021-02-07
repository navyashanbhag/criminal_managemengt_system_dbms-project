from tkinter import Tk

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication
import sys
import mysql.connector as mysql
from criminal_record import ConnectorDb
#from homepage import home
# from main_admin_page import UiAdminWindow

# connecting to database
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="maravanthe2001",
    database="criminal",
    port="3306"
)
cursor = db.cursor()


# function to initialize the database
def init_db():
    cursor.execute("SHOW TABLES;")
    for x in cursor:
        print(x)


# log in window class
class UiMainWindow(object):
    # initializing class constructor and login page
    def __init__(self):


        # self.ui = ConnectorDb
        # self.next_window = QtWidgets.QMainWindow()
        self.font = QtGui.QFont()
        self.font.setFamily("Calibri")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        init_db()

    # Log in Window creation
    # noinspection PyAttributeOutsideInit
    def setup_ui(self, main_window):
        # Main Window
        main_window.setObjectName("MainWindow")
        main_window.resize(450,300)
        main_window.setMinimumSize(QtCore.QSize(650, 200))
        main_window.setMaximumSize(QtCore.QSize(650, 200))

        # main_window.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.admin_login_msg = QtWidgets.QLabel(self.centralwidget)
        self.admin_login_msg.setFont(self.font)
        self.admin_login_msg.setObjectName("admin_login_msg")
        self.verticalLayout.addWidget(self.admin_login_msg)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")

        self.password_lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit_2.setFont(self.font)
        self.password_lineEdit_2.setObjectName("password_lineEdit_2")
        self.gridLayout.addWidget(self.password_lineEdit_2, 1, 1, 1, 1)
        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setFont(self.font)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.gridLayout.addWidget(self.username_lineEdit, 0, 1, 1, 1)

        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setFont(self.font)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        # creating cancel button
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setFont(self.font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.on_pressed_cancel)
        self.gridLayout.addWidget(self.cancel_btn, 2, 0, 1, 1)

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setFont(self.font)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)

        # creating submit button
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setFont(self.font)
        self.submit_btn.setObjectName("submit_btn")
        self.submit_btn.clicked.connect(self.on_pressed_submit)
        self.gridLayout.addWidget(self.submit_btn, 2, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        main_window.setCentralWidget(self.centralwidget)
        self.re_translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # setting the text of elements of main window
    def re_translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Log in"))
        self.admin_login_msg.setText(_translate("MainWindow", "Admin Log in"))
        self.username_label.setText(_translate("MainWindow", "Username :"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))

    # function to open main admin page window
    def open_next_window(self):
        MainWindow.hide()
        root = Tk()
        self.ui = ConnectorDb(root)
        root.mainloop()
        self.ui.setup_ui(self.next_window)
        self.next_window.show()


    #def homewindow(self):
      #  MainWindow.hide()
       # home()

    # checking whether password is correct or not
    def check_validity(self, username, password):
        valid_list = []
        sql_cmd = "SELECT * FROM criminal.admin where admin_name = %s and password=%s ;"
        cursor.execute(sql_cmd, (username, password))
        for x in cursor:
            # print(x)
            valid_list.append(x)
            print(valid_list)
            # print(valid_list)
        if valid_list:
            print("login successfully")
            success_msg = QMessageBox(QMessageBox.Information, "Login Successfully",
                                      """You have logged in successfully as """ +
                                      str(username),
                                      QMessageBox.Ok, QApplication.activeWindow())
            success_msg.setTextFormat(Qt.RichText)
            success_msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
            success_msg.exec()
            self.open_next_window()
            #self.homewindow()
        else:
            print("login failed")
            failed_msg = QMessageBox(QMessageBox.Critical, "Login failed",
                                     """Incorrect username or password""",
                                     QMessageBox.Ok, QApplication.activeWindow())
            failed_msg.setTextFormat(Qt.RichText)
            failed_msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
            failed_msg.exec()

    # on pressed submit button
    def on_pressed_submit(self):
        in_username = self.username_lineEdit.text()
        in_password = self.password_lineEdit_2.text()
        print("pressed submit button")
        print("Username = " + in_username)
        print("Password = " + in_password)
        self.check_validity(username=in_username, password=in_password)

    # on pressed cancel button
    @staticmethod
    def on_pressed_cancel():
        print("cancel button clicked")
        app.quit()


# main function program starts from here
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = UiMainWindow()
        ui.setup_ui(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except mysql.Error as e:
        print("Error : " + str(e))
