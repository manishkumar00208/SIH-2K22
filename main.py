import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5.uic import loadUi
import pyrebase



firebaseConfig={
    'apiKey': "AIzaSyBAFvLNstbRGfM58UzIoSWcWXyguuNz2rA",
  'authDomain': "sihdb-f52f5.firebaseapp.com",
  'databaseURL': "https://sihdb-f52f5-default-rtdb.firebaseio.com",
  'projectId': "sihdb-f52f5",
  'storageBucket': "sihdb-f52f5.appspot.com",
  'messagingSenderId': "133132355449",
  'appId': "1:133132355449:web:ef24dcc659e801dcc791a8"
}


firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

def backButton(val):
    widget.removeWidget(val)
    widget.setCurrentIndex(widget.currentIndex())

class Intro(QDialog):
    def __init__(self):
        super(Intro,self).__init__()
        loadUi("intro.ui",self)
        
        self.login.clicked.connect(self.loginFunction)
        self.signup.clicked.connect(self.signupFunction)

    def loginFunction(self):
        login=Login()

        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

    def signupFunction(self):
        signup=SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.login.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back.clicked.connect(lambda:backButton(self))


    def loginFunction(self):
        username=self.username.text()
        password=self.username.text()
        if username == "s" and password=="s":
            add=AddOrUpdate()

            widget.addWidget(add)
            widget.setCurrentIndex(widget.currentIndex() + 1)

            

class SignUp(QDialog):
    def __init__(self):
        super(SignUp,self).__init__()
        loadUi("signup.ui",self)
        self.signup.clicked.connect(self.signupFunction)
        self.back.clicked.connect(lambda:backButton(self))

        

    def signupFunction(self):
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    

class NewVolunteer(QDialog):
    def __init__(self):
        super(NewVolunteer,self).__init__()
        loadUi("newVolunteer.ui",self)
        self.create.clicked.connect(self.newVolunteer)
        self.back.clicked.connect(lambda:backButton(self))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)


    def newVolunteer(self):
        name=self.name.text()
        age=self.age.text()
        aadhar=self.aadhar.text()
        MOBILE=self.mobile.text()
        qualification=self.qualification.text()
        password=self.password.text()
        confirm=self.confirm.text()
        village=self.village.text()
        
        gender=self.gender.currentText()
        if(password==confirm):
            db.child('volunteer').push({'name':name,'age':age,'aadhar':aadhar,'mobile':MOBILE,'qualification':qualification,'password':password,'village':village,'gender':gender})
            msg=QMessageBox()
            msg.setWindowTitle('Success')
            msg.setText("Created new volunteer with name = "+ name)

            x=msg.exec()
            app.exit()
        else:
            msg=QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText("Password doesn't match")

            x=msg.exec()


            
class NewScholar(QDialog):
    def __init__(self):
        super(NewScholar,self).__init__()
        loadUi("newscholar.ui",self)
        self.create.clicked.connect(self.newScholar)
        self.back.clicked.connect(lambda:backButton(self))

        
    def newScholar(self):
        name=self.name.text()
        age=self.age.text()
        place=self.place.text()
        address=self.address.text()
        pin=self.pincode.text()
        state=self.state.text()
        aadhar=self.aadhar.text()
        bankAc=self.bankac.text()
        bankName=self.bankname.text()
        IFSC=self.IFSC.text()
        Email=self.email.text()
        MOBILE=self.mobile.text()
        qualification=self.qualification.text()
        if self.yes.isChecked():
            PWD='yes'
        else:
            PWD='no'

        reservation=self.reservation.text()
        gender=self.gender.currentText()
        status="Pending"
        amount=""
        


        db.child('beneficiary').push({'name': name,'age':age,"place":place,'address':address,'pin':pin,'state':state,'aadhar':aadhar,'bankAc':bankAc,'bankName':bankName,
    'IFSC':IFSC,'Email':Email,'MOBILE':MOBILE,'qualification':qualification,'PWD':PWD,'reservation':reservation,'gender':gender,'status':status,'amount':amount})



class UpdateScholarPage(QDialog):
    def __init__(self,selected):
        super(UpdateScholarPage,self).__init__()
        loadUi("updateScholar.ui",self)
        self.back.clicked.connect(lambda:backButton(self))

        self.name.setText(selected.val()['name'])
        self.aadhar.setText(selected.val()['aadhar'])
        self.age.setText(selected.val()['age'])
        self.place.setText(selected.val()['place'])
        self.address.setText(selected.val()['address'])
        self.pincode.setText(selected.val()['pin'])
        self.state.setText(selected.val()['state'])
        self.IFSC.setText(selected.val()['IFSC'])
        self.email.setText(selected.val()['Email'])
        self.mobile.setText(selected.val()['MOBILE'])
        self.qualification.setText(selected.val()['qualification'])
        self.reservation.setText(selected.val()['reservation'])
        self.status.setCurrentText(selected.val()['status'])
        self.amount.setText(selected.val()['amount'])
        self.gender.setCurrentText(selected.val()['gender'])
        self.bankac.setText(selected.val()['bankAc'])
        self.bankname.setText(selected.val()['bankName'])
        if selected.val()['PWD']=='yes':
            self.yes.setChecked(True)
        else:
            self.yes.setChecked(True)





        


class UpdateScholar(QDialog):
    def __init__(self):
        super(UpdateScholar,self).__init__()
        loadUi("chooseBeneficiary.ui",self)
        self.back.clicked.connect(lambda:backButton(self))
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,400)
        self.loadData()
        self.tableWidget.itemClicked.connect(self.detailsFunction)

    def detailsFunction(self):
        item=self.tableWidget.currentItem()
        selectedRow=item.row()
        details=UpdateScholarPage(self.peoples[selectedRow])
        widget.addWidget(details)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    peoples=db.child('beneficiary').get()

    def loadData(self):
        
        row=0
        self.tableWidget.setRowCount(len(self.peoples.val()))
        for person in self.peoples:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(person.val()["name"]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(person.val()["place"]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(person.val()["aadhar"]))

            row=row+1

class EditVolunteerPage(QDialog):
    def __init__(self,selected):
        super(EditVolunteerPage,self).__init__()
        loadUi("updateVolunteer.ui",self)
        self.back.clicked.connect(lambda:backButton(self))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)

        
        self.name.setText(selected['name'])
        self.aadhar.setText(selected['aadhar'])
        self.age.setText(selected['age'])
        self.place.setText(selected['place'])
        self.address.setText(selected['address'])
        self.pincode.setText(selected['pin'])
        self.state.setText(selected['state'])
        self.IFSC.setText(selected['IFSC'])
        self.Email.setText(selected['email'])
        self.mobile.setText(selected['mobile'])
        self.qualification.setText(selected['qualification'])
        self.reservation.setText(selected['reservation'])
        self.status.setText(selected['status'])
        self.amount.setText(selected['amount'])
        self.gender.setCurrentText(selected['gender'])


        if(self.password.text()==self.confirm.text()):
            db.child('volunteer').push({'name':self.name.text(),'age':self.age.text(),'aadhar':self.aadhar.text(),'mobile':self.mobile.text(),'qualification':self.qualification.text(),'password':self.password.text(),'village':self.village.text(),'gender':self.gender.text()})
            msg=QMessageBox()
            msg.setWindowTitle('Success')
            msg.setText("Created new volunteer with name = "+ self.name.text())

            x=msg.exec()
            app.exit()
        else:
            msg=QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText("Password doesn't match")

            x=msg.exec()

class EditVolunteer(QDialog):
    def __init__(self):
        super(EditVolunteer,self).__init__()
        loadUi("chooseVolunteer.ui",self)
        self.back.clicked.connect(lambda:backButton(self))
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,400)
        self.loadData()
        self.tableWidget.itemClicked.connect(self.detailsFunction)
        

    def detailsFunction(self):
        item=self.tableWidget.currentItem()
        selectedRow=item.row()
        details=UpdateScholarPage(self.peoples[selectedRow])
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

  
class AddOrUpdate(QDialog):
    def __init__(self):
        super(AddOrUpdate,self).__init__()
        loadUi("addorupdate.ui",self)
        newsch=NewScholar()
        newVol=NewVolunteer()
        self.newsch.clicked.connect(lambda:self.buttonFunction(newsch))
        self.newvol.clicked.connect(lambda:self.buttonFunction(newVol))
        self.editvol.clicked.connect(lambda:self.buttonFunction(EditVolunteer()))
        self.updsch.clicked.connect(lambda:self.buttonFunction(UpdateScholar()))
        self.back.clicked.connect(lambda:backButton(self))



    def buttonFunction(self,val):
        widget.addWidget(val)
        widget.setCurrentIndex(widget.currentIndex() + 1)   
            
         

app=QApplication(sys.argv)
mainwindow=Intro()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(840)
widget.setFixedWidth(1080)
widget.show()

app.exec()
