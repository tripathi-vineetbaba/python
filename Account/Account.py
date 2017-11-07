import Person_Class
import random

class Accounts:
    p1=Person_Class.Person()
    accNo=00000
    def __init__(self,accNo,p1):
        self.accNo=accNo
        self.p1=p1
    def viewAcc(self):
        return self.accNo
    def viewPerson(self):
        return self.p1
    def generateAcc():
        temp=random.randint(10000198, 99895598)
        return temp