from select import select
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class Submit(QDialog):
    def __init__(self):
        super(Submit,self).__init__()
        loadUi("volunteer.ui",self)
        self.submit.clicked.connect(self.submitFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def submitFunction(self):
        username=self.username.text()
        password=self.password.text()
        print(username+password)
        table=VolunteerTable()
        widget.addWidget(table)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class VolunteerTable(QDialog):
    def __init__(self) :
        super(VolunteerTable,self).__init__()
        loadUi("table.ui",self)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,400)
        self.loadData()
        self.tableWidget.itemClicked.connect(self.detailsFunction)

    def detailsFunction(self):
        item=self.tableWidget.currentItem()
        selectedRow=item.row()
        details=personDetails(self.peoples[selectedRow])
        widget.addWidget(details)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    peoples=[{"name":"John","age":"45","address":"NewYork"},
        {"name":"John","age":"45","address":"NewYork"},
        {"name":"AI","age":"45","address":"NewYork"},
        {"name":"John","age":"45","address":"NewYork"},
        {"name":"John","age":"45","address":"NewYork"},
        {"name":"John","age":"45","address":"NewYork"},
        {"name":"John","age":"45","address":"NewYork"}
        ]  

    def loadData(self):
        
        row=0
        self.tableWidget.setRowCount(len(self.peoples))
        for person in self.peoples:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(person["address"]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(person["age"]))

            row=row+1


class personDetails(QDialog):
    def __init__(self,selected):
        super(personDetails,self).__init__()
        loadUi("personDetails.ui",self)
        details=selected
        
        self.nameLabel.setText(selected['name'])
        self.addressLabel.setText(selected['address'])
        self.login.clicked.connect(self.loginFunction)
    
    def loginFunction(self):
        intro=Intro()
        widget.addWidget(intro)
        widget.setCurrentIndex(0)


class Intro(QDialog):
    def __init__(self) :
        super(Intro,self).__init__()
        loadUi("intro.ui",self)
        self.volunteerButton.clicked.connect(self.volunteerButtonClicked)

    def volunteerButtonClicked(self):
        volunteerPage=Submit()
        widget.addWidget(volunteerPage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app=QApplication(sys.argv)
mainwindow=Intro()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(680)
widget.setFixedWidth(720)
widget.show()

app.exec()



#self.tableWidget.setHorizontalLabels({"","",""})
#def loadData(self):
#   connection=sqlite3.connect("data.sqlite")
#   cur=connection.cursor()
#   sqlquery = "SELECT * FROM --------"
#   
#   self.tableWidget.setRowCount(50)
#   tablerow=0
#
#   for row in cur.execute(sqlquery):
#       self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
#       self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[0]))
#       self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[0]))
#       tablerow+=1
#
