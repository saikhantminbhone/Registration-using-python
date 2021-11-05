#! C:\Python36\python.exe
import MySQLdb as mysql #import MySQL 8.0 server to connnect the database
import cgi #import cg gateway
import cgitb;cgitb.enable #enable to track cgi error. cgi tb request for debugging
from saikhantminbhone_oop_class import*

form=cgi.FieldStorage()

#b1 = coursemaster()
#db = b1.saidb()


#b1.sai("C++","C++ is a programming language",db)



r1 = studentmaster()
db = r1.saidb()

r1.minn("saikhant","khant","saikhanbhone@gmail.com","male","mandalay","09766577999",55,1,db)
