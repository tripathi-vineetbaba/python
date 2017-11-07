#Create Person class with below attributes
#Name, mobile no, address, office address, email id
#view, update, add, delete

class Person:
    name=""
    mobile=0000000000
    address=""
    office=""
    email=""
    aadhar=""
    def __init__(self,name=None,mobile=None,address=None,office=None,email=None,aadhar=None):
        self.name=name
        self.mobile=mobile
        self.address=address
        self.office=office
        self.email=email
        self.aadhar=aadhar
    def viewaadhar(self):
        return self.aadhar
    def addAadhar(self,aadhar):
        self.aadhar=aadhar
    def viewName(self):
        return self.name
    def viewAdd(self):
        return self.address
    def viewOffice(self):
        return self.office
    def viewEmail(self):
        return self.email
    def addName(self,name):
        self.name=name
    def addMobile(self,mobile):
        self.mobile=mobile
    def addaddress(self,address):
        self.address=address
    def addoffice(self,office):
        self.office=office
    def addemail(self,email):
        self.email=email
    def viewMobile(self):
        return self.mobile
    def createPerson(self,name=None, mobile=None, address=None, office=None, email=None, aadhar=None):
        p1 = Person(name, mobile, address, office, email, aadhar)
        return p1
