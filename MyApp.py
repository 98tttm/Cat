from PyQt6.QtWidgets import QApplication, QMainWindow

from EmployeeManagement.ui.MainWindow_EmployeeManagementExt import MainWindow_EmployeeManagementExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow_EmployeeManagementExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()