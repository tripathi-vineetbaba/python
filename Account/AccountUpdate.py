import os
import Account
import createPerson

acclist=list()

def addAcc():
        p1 = createPerson.retPer()
        accNo = Account.Accounts.generateAcc()
        aco1 = Account.Accounts(accNo,p1)
        print ("Account has been created successfully.")
        print("Account Number is: ",accNo)
        acclist.append(aco1)

def viewAcc():
        return acclist

def updateName(acc):
        accList=viewAcc()
        for x in range(0,len(acclist),1):
            if(accList[x].viewAcc()==acc):
                print("Account holder is %s" %(accList[x].viewPerson().viewName()))
                newName=input("Enter Name to update: ")
                accList[x].viewPerson().addName(newName)


def updateMobile(acc):
    accList = viewAcc()
    for x in range(0, len(acclist), 1):
        if (accList[x].viewAcc() == acc):
            print("Account holder is %s" %(accList[x].viewPerson().viewName()))
            print("Mobile:  %s" %(str(accList[x].viewPerson().viewMobile())))
            newName = input("Enter Mobile to update: ")
            accList[x].viewPerson().addMobile(newName)

def updateEmail(acc):
        accList = viewAcc()
        for x in range(0, len(acclist), 1):
            if (accList[x].viewAcc() == acc):
                print("Account holder is %s" % (accList[x].viewPerson().viewName()))
                print("Email:  %s" %(str(accList[x].viewPerson().viewEmail())))
                newName = input("Enter Email to update: ")
                accList[x].viewPerson().addemail(newName)

def updateAadhar(acc):
        accList = viewAcc()
        for x in range(0, len(acclist), 1):
            if (accList[x].viewAcc() == acc):
                print("Account holder is %s" % (accList[x].viewPerson().viewName()))
                print("Aadhar:  %s" %(str(accList[x].viewPerson().viewaadhar())))
                newName = input("Enter Aadhar to update: ")
                accList[x].viewPerson().addAadhar(newName)

def updateOffice(acc):
        accList = viewAcc()
        for x in range(0, len(acclist), 1):
            if (accList[x].viewAcc() == acc):
                print("Account holder is %s" % (accList[x].viewPerson().viewName()))
                print("Office Address:  %s" %(str(accList[x].viewPerson().viewOffice())))
                newName = input("Enter Address to update: ")
                accList[x].viewPerson().addoffice(newName)

def updateAddress(acc):
        accList = viewAcc()
        for x in range(0, len(acclist), 1):
            if (accList[x].viewAcc() == acc):
                print("Account holder is %s" % (accList[x].viewPerson().viewName()))
                print("Aadhar:  %s" %(str(accList[x].viewPerson().viewAdd())))
                newName = input("Enter Aadhar to update: ")
                accList[x].viewPerson().addaddress(newName)

