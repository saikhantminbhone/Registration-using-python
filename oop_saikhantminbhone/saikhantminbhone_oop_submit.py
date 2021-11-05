#! C:\Python36\python.exe
import MySQLdb as mysql
import cgi
import cgitb;cgitb.enable()
from saikhantminbhone_oop_class import * #importing Student Class from the student module

print("Content-type:text/html\n\n")

form=cgi.FieldStorage()
def bhone(input):
    if input in form:
        return form[input].value
    
if "submitted" in form:
    fname=bhone("txtfname")
    lname=bhone("txtlname")
    email=bhone("txtemail")
    gender=bhone("gender")
    address=bhone("txtaddress")
    phone=bhone("txtcontactnumber")
    password=bhone("txtcpassword")
    course=bhone("txtdropdown")

#object creation from Student Class
    Student1 = studentmaster()
    db = Student1.saidb()

#calling insert function from the Student Class
#It is the porlymorphism because we use the same name of method in the coursemaster class and Student class. But the implementations are different.
    Student1.minn(fname,lname,email,gender,address,phone,password,course,db)       
