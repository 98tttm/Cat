from EmployeeManagement.ui.MainWindow_EmployeeManagement import Ui_TRANTHANHTHINH_K234111418_K234111E


class MainWindow_EmployeeManagementExt(Ui_TRANTHANHTHINH_K234111418_K234111E):

    salary_intern = 2000000
    salary_fresher = 10000000
    salary_junior = 15000000
    salary_senior = 30000000

    num_intern = 0
    num_fresher = 0
    num_junior = 0
    num_senior = 0

    money_intern = 0
    money_fresher = 0
    money_junior = 0
    money_senior = 0

    def setupUi(self, TRANTHANHTHINH_K234111418_K234111E):
        super().setupUi(TRANTHANHTHINH_K234111418_K234111E)
        self.MainWindow=TRANTHANHTHINH_K234111418_K234111E
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSalary.clicked.connect(self.process_salary)
        self.pushButtonNext.clicked.connect(self.Next)
        self.pushButtonExt.clicked.connect(self.Exit)
    def Exit(self):
        self.MainWindow.close()
    def Next(self):
        self.lineEditNumberOfEmployee.setText("")
        self.lineEditNumberOfEmployee.setFocus()


    def process_salary(self):
        num_employee = 0
        try:
            num_employee = int(self.lineEditNumberOfEmployee.text())
        except:
            num_employee = 0
        if self.radioButtonIntern.isChecked():
            salary_money_intern = num_employee*self.salary_intern
            self.num_intern = self.num_intern+num_employee
            self.money_intern = self.money_intern + salary_money_intern
        elif self.radioButtonJunior.isChecked():
            salary_money_junior = num_employee * self.salary_junior
            self.num_junior = self.num_junior + num_employee
            self.money_junior = self.money_junior + salary_money_junior
        elif self.radioButtonSenior.isChecked():
            salary_money_senior = num_employee * self.salary_senior
            self.num_senior = self.num_senior + num_employee
            self.money_senior = self.money_senior + salary_money_senior
        elif self.radioButtonFresher.isChecked():
            salary_money_fresher = num_employee * self.salary_fresher
            self.num_fresher = self.num_fresher + num_employee
            self.money_fresher = self.money_fresher + salary_money_fresher

        self.lineEditNumberofInternEmployee.setText(str(self.num_intern))
        self.lineEditNumberofFresherEmployee.setText(str(self.num_fresher))
        self.lineEditNumberofJuniorEmployee.setText(str(self.num_junior))
        self.lineEditNumberofSeniorEmployee.setText(str(self.num_senior))
        self.lineEditNumberofAllEmployee.setText(str(self.num_senior + self.num_intern + self.num_junior + self.num_fresher))
        self.lineEditSalaryIntern.setText(str(self.money_intern))
        self.lineEditSalaryJunior.setText(str(self.money_junior))
        self.lineEditSalaryFresher.setText(str(self.money_fresher))
        self.lineEditSalarySenior.setText(str(self.money_senior))
        self.lineEditSalaryAll.setText(str(self.money_intern + self.money_junior + self.money_fresher + self.money_senior))