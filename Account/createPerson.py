import Person_Class
def retPer():

    name = input("  Account holder's Name: ")
    mobile = input("              Mobile No: +91")
    aadhar = input("          Aadhar Number: ")
    email = input("               Email Id: ")
    office = input("   Enter Office address: ")
    address = input("Enter permanent address: ")
    p1=Person_Class.Person()
    return p1.createPerson(name,mobile,address,office,email,aadhar)
    '''
    name ="Vineet Tripathi"
    mobile =8400001004
    aadhar =7887897897
    email ="testmail"
    office = "offaddress"
    address = "homeaddress"
    p1=Person_Class.Person()
    return p1.createPerson(name,mobile,address,office,email,aadhar)
    '''
