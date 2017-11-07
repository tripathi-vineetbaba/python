import display
cho='y'
while (cho == 'Y' or cho =='y'):
    print("\t\t1. Add Account")
    print("\t\t2. View Account")
    print("\t\t3. Update Details")
    print ("\t\t4. Delete")
    ch=input("\t\tEnter choice: ")
    chi=int(ch)
    if(chi==1):
        display.add()
    elif(chi==2):
        display.view()
    elif (chi==3):
        display.update()
    elif(chi==4):
        display.delete()
    else:
        print("Invalid Choice!!!")
    cho=input("\t\tEnter [Y/y] to continue, [N/n] to cancel: ")