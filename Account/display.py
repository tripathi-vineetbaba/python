import AccountUpdate,os
def displayAcc(accNo):
    acc = AccountUpdate.viewAcc()
    if (len(acc) == 0):
        print("No Account has been created yet. Please create one and then proceed.")
    else:
        for x in range(0, len(acc), 1):
            if (acc[x].viewAcc() == accNo):
                print("\t\tAccount holder:   %s " % (acc[x].viewPerson().viewName()))
                print("\t\tMobile No:        %s" % (str(acc[x].viewPerson().viewMobile())))
                print("\t\tAccount Number:   %s" % str(acc[x].viewAcc()))
                print("\t\tAddress:          %s" % (acc[x].viewPerson().viewAdd()))
                print("\t\tEmail:            %s" % (acc[x].viewPerson().viewEmail()))
                print("\t\tAadhar No:        %s" % (str(acc[x].viewPerson().viewaadhar())))


def displayAll():
    acc = AccountUpdate.viewAcc()
    if(len(acc)==0):
        print("No Account has been created yet. Please create one and then proceed.")
    else:
        os.system("cls")
        for x in range (0,len(acc),1):
            print("******************************************Customer %s********************************************************************" % str(x + 1))
            print("\t\tAccount holder:   %s " % (acc[x].viewPerson().viewName()))
            print("\t\tMobile No:        %s" % (str(acc[x].viewPerson().viewMobile())))
            print("\t\tAccount Number:   %s" % str(acc[x].viewAcc()))
            print("\t\tAddress:          %s" % (acc[x].viewPerson().viewAdd()))
            print("\t\tEmail:            %s" % (acc[x].viewPerson().viewEmail()))
            print("\t\tAadhar No:        %s" % (str(acc[x].viewPerson().viewaadhar())))





def add():
    AccountUpdate.addAcc()

def view():
    print("\t\tPlease choose from below options:")
    print("\t\t1. View details from Account Number")
    ch=int(input("\t\t2. View details of All account holder\n"))

    if (ch==1):
        acc=int(input("\t\tEnter Acc Number to find details: "))
        displayAcc(acc)
    elif(ch==2):
        displayAll()
    else:
        print("\t\t\tInvalid Option!!!")

def update():
    print("\t\tPlease choose from below options:")
    print("\t\t1. Update Name")
    print("\t\t2. Update Mobile No")
    print("\t\t3. Update Aadhar")
    print("\t\t4. Update Email")
    print("\t\t5. Update Office Address")
    ch=int(input("\t\t6. Update residence address"))
    acc=int(input("\t\tEnter account number to update details: "))
    if(ch==1):
        AccountUpdate.updateName(acc)
    elif(ch==2):
        AccountUpdate.updateEmail(acc)
    elif(ch==3):
        AccountUpdate.updateAadhar(acc)
    elif(ch==4):
        AccountUpdate.updateEmail(acc)
    elif(ch==5):
        AccountUpdate.updateOffice(acc)
    elif(ch==6):
        AccountUpdate.updateAddress(acc)
    else:
        print("\t\t\tInvalid Option!!!")

def delete():
    ch=int(input("\t\tEnter Account No to delete the recored: "))
    acc = AccountUpdate.viewAcc()
    for x in range(0, len(acc)-1, 1):
        if (acc[x].viewAcc() == ch):
            AccountUpdate.viewAcc().pop(x)


