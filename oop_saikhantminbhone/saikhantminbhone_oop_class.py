#! C:\Python36\python.exe
import MySQLdb as mysql #import MySQL 8.0 server to connnect the database
import cgi #import cg gateway
import cgitb;cgitb.enable #enable to track cgi error. cgi tb request for debugging

form=cgi.FieldStorage()
#create database class to connect the database
class database:
    def saidb(self):
        db = mysql.connect(host="localhost", user="root", password="admin", db="db_oop_saikhantminbhone")
        #print("Database is now connected")
        return db
#create coursemaster class to insert and retrieve the data from the database
#using inheritance, coursemster class is instantiated from database
class coursemaster(database):
    def sai(self,course_name,course_description,db):
        self.coursename = course_name
        self.coursedes = course_description

        sql = "INSERT INTO `tbl_saikhantminbhone_coursemaster` (`course_name`, `course_description`) VALUES ('{0}', '{1}')".format(self.coursename,self.coursedes)

        cursor = db.cursor()
        try:
            cursor.execute(sql)
            print("Data is sucessfully saved into database");
            db.commit()
        except Exception as e:
            print(str(e))
            db.rollback()

    def khant(self,cursor):                                                        
        sql = "SELECT course_id,course_name FROM `tbl_saikhantminbhone_coursemaster`"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            row = cursor.fetchone()


class studentmaster(database):
    def minn(self,student_firstname,student_lastname,email,gender,residential_address,contact_no,password,course_id,db):
        self.student_firstname = student_firstname
        self.student_lastname = student_lastname
        self.email = email
        self.gender = gender
        self.residential_address = residential_address
        self.contact_no = contact_no
        self.password = password
        self.course_id = course_id

        sql = "INSERT INTO `tbl_saikhantminbhone_studentmaster` (`student_firstname`, `student_lastname`, `email`, `gender`, `residential_address`, `contact_no`,`password`, `course_id`) VALUES ('{0}', '{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(self.student_firstname,self.student_lastname,self.email,self.gender,self.residential_address,self.contact_no,self.password,self.course_id)

        cursor = db.cursor()
        try:
            cursor.execute(sql)
            print("""
<!DOCTYPE html>
    <head>
        <title>saikhant.com</title>
    <style>
         body {
		background-image: url("register.jpg");
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
                         width:100%;
    }
    h1 {
        font-size: 30;
        text-align: center;
        color: white;
        margin-top: 100px;
    }
    </style>
    </head>
    <body>
            <h1 class="h1"> Thank you for your registration</h1>
    </body>
</html>""");
            db.commit()
        except Exception as e:
            print(str(e))
            db.rollback()
    

