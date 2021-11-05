#! C:\Python36\python.exe
import MySQLdb as mysql #import MySQL 8.0 server to connect the database
import cgi #import cgi gateway
import cgitb;cgitb.enable() #enable to track cgi error.cgi tb request for debugging
from saikhantminbhone_oop_class import*

print("Content-type:text/html\n\n")

form=cgi.FieldStorage()

r1 = coursemaster()
db = r1.saidb()
cursor = db.cursor()

r1.khant(cursor)

print("""
<!DOCTYPE html>
<head>
    <title> wwwabclearingcentre.com</title>
    <style>
        body {
		background-image: url("register.jpg");
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
                         width:100%;
	}
 .signup
        {
            background-color:ACBCD5;
            background-color: aliceblue;
            width: 500px;
            margin-top:70px;
            text-align: center;
            
    }
    </style>
</head>

<body >
   <center>
    <!--Form-->
    <form name="saikhant" action="saikhantminbhone_oop_submit.py" onsubmit="return validate()" class="signup" >
            <h1 >Registration Form</h1>
    <!--Userfirstname Input Control-->
    <table >
            <tr>
                    <td>Student First Name:</td>
                    <td><input type="text" name="txtfname" id="txtfname" onblur="checkblank('txtfname','error_fname')"></td>
                    <!--this is tooltip for first name -->
                    <td><span title="User first name must be fill">&#63;</span></td>
                    <td><p id="error_fname" style="color:red;"></p></td>
                </tr>
                <!--Userlastname Input Control-->
                <tr>
                    <td>Student Last Name:</td>
                    <td><input type="text" name="txtlname" id="txtlname" onblur="checkblank('txtlname','error_lname')"></td>
                    <!--this is tooltip for last name -->
                    <td><span title="User Last name must be fill">&#63;</span></td>
                    <td><p id="error_lname" style="color:red;"></p></td>
                </tr>
                <!--Useremail address Input Control-->
                <tr>
                    <td>Email address:</td>
                    <td><input type="text" name="txtemail" id="txtemail" onblur="checkemail()"></td>
                    <!--this is tooltip for email address -->
                    <td><span title="Email have to put and must include @ sign and . sign">&#63;</span></td>
                    <td><p id="error_email" style="color:red;"></p></td>
                </tr>
                <!--User genter  Input Control-->
                <tr>
                    <td>Gender:</td>
                    <td>
                    <input type="radio" name="gender" id="male" value="male"> Male
            
                    <input type="radio" name="gender" id="female" value="female">Female
                    </td>
                        <!--this is tooltip for gender -->
                                <td><span title="Please choose gender">&#63;</span></td>
                    <td><p id="error_gender" style="color:red;"></p></td>
                </tr>
                <!--User address Input Control-->
                <tr>
                    <td>Residential address:</td>
                    <td><textarea name="txtaddress" id="txtaddress" onblur="checkblank('txtaddress','error_address')"></textarea></td>
                    <!--this is tooltip address-->
                    <td><span title="User have to fill user address">&#63;</span></td>
                    <td><p id="error_address" style="color:red;"></p></td>
                </tr>
                <!--user contact number  Input Control-->
                <tr>
                    <td>Contact Number:</td>
                    <td><input type="text" name="txtcontactnumber" id="txtcontactnumber" onblur="checkblank('txtcontactnumber','error_contactnumber')" ></td>
                    <!--this is tooltip for contact number -->
                    <td><span title="Username have to fill contact and have at most 11 digits">&#63;</span></td>
                    <td><p id="error_contactnumber" style="color:red;"></p></td>
                <tr>    
                        <!--using dropdown list-->    
                        <td>Choose courses</td>    
                        <td><select name="txtdropdown" id="txtdropdown" onblur="checkblank('txtdropdown','error_courses')">     
                        """)
for (course_id, course_name) in cursor:
    print('<option value="'+ str(course_id)+'">'+ course_name +'</option>')
print("""
		</select>
		</td>
                    <td><span title="choose courses">&#63;</span></td>
                    <td><p id="error_courses" style="color:red;"></p></td>
             </tr>
                <!--Password input control-->
                <tr>
                    <td>Password:</td>
                    <td><input type="password" name="txtpassword" id="txtpassword" onblur="checkblank('txtpassword','error_password')"> </td>
                    <!--this is tooltip for password-->
                    <td><span title="Please enter password">&#63;</span></td>
                    <td><p id="error_password" style="color:red;"></p></td>
                </tr>
                <!--confirm Password input control-->
                <tr>
                    <td>Confirm Password:</td>
                    <td><input type="password" name="txtcpassword" id="txtcpassword" onblur="checkblank('txtcpassword','error_cpassword')"> </td>
                    <!--this is tooltip for password-->
                    <td><span title="Please enter confirm password">&#63;</span></td>
                    <td><p id="error_cpassword" style="color:red;"></p></td>
                </tr>
                <!--Buttons-->
                <tr>
                        <td><input type="hidden" name="submitted" value="1"></td>
                        <td><input type="submit" name="submit" value="SUBMIT"></td>
                        <td><input type="reset" name="reset" value="RESET"></td>
                    </tr>
            
                </table>
                </form>
            </center>
            </body>
            <!--javascript start here-->
            <!--validate function for submit click-->
            <script>
                function validate()
                {
                    var input=true;
                    
                    var fname = document.forms["saikhant"]["txtfname"].value;
                    if(fname=="")
                    {
                        document.getElementById("error_fname").innerHTML="Please enter your first name";
                        input=false;
                    }
                    else if (!checklength(fname,1,50))
                    {
                        document.getElementById("error_fname").innerHTML="Please enter under 50 character";
                        input=false;
                    }
                    else
                    {
                        document.getElementById("error_fname").innerHTML="";
                    }
                    
            
                    var lname = document.forms["saikhant"]["txtlname"].value;
                    if(lname=="")
                    {
                        document.getElementById("error_lname").innerHTML="Please enter your last name";
                        input=false;
                    }
                    else if (!checklength(lname,1,50))
                    {
                        document.getElementById("error_lname").innerHTML="Pleae enter under 50 character";
                        input=false;
                    }
                    else
                    {
                        document.getElementById("error_lname").innerHTML="";
                    }
            
            
                    var email = document.forms["saikhant"]["txtemail"].value;
                    if(email=="")
                    {
                        document.getElementById("error_email").innerHTML="Please enter your email address";
                        input=false;
                    }
                    else
                    {
                        document.getElementById("error_email").innerHTML="";
                    }
                   
                   
                    var a = document.getElementById("male").checked;
                    var b = document.getElementById("female").checked;
                    if (a == false && b == false){
                        document.getElementById("error_gender").innerHTML="Please choose gender";
                    input = false;
                }
                   
                
                    else
                    { document.getElementById("error_gender").innerHTML="";
                    }
                
                    var address = document.forms["saikhant"]["txtaddress"].value;
                    if(address=="")
                    {
                        document.getElementById("error_address").innerHTML="Please enter your address";
                        input=false;
                    }
                    else
                    {
                        document.getElementById("error_address").innerHTML="";
                    }
                    
                   

                    var contactnumber = document.forms["saikhant"]["txtcontactnumber"].value;
                    if(contactnumber=="")
                    {
                        document.getElementById("error_contactnumber").innerHTML="Please enter your contact number";
						input=false;
                    }
                    else if (!checklength(contactnumber,11,11))
                    {
                        document.getElementById("error_contactnumber").innerHTML="contact number must be at most 11 digts";
                        input=false;
                    }
                    else if(!contactnumber.match(/^[0-9]+$/))
                    {
                        document.getElementById("error_contactnumber").innerHTML="Please enter number only";
                        input=false;
                    }
                    else
                    {
                        document.getElementById("error_contactnumber").innerHTML="";
                    }
                    
                    var password = document.forms["saikhant"]["txtpassword"].value;
                    var cpassword=document.forms["saikhant"]["txtcpassword"].value;
                    if(password=="" )
                    {
                        document.getElementById("error_password").innerHTML="Please enter your password";
                        input=false
                    }
                    else if (cpassword=="")
                    {
                        document.getElementById("error_cpassword").innerHTML="Please enter confirm password";
                        input=false
                    }
                    else if ( password != cpassword)
                    {
                        document.getElementById("error_cpassword").innerHTML="Password don't match"
                        input=false
                    }
                    else 
                    {
                        document.getElementById("error_password").innerHTML="";
                        document.getElementById("error_cpassword").innerHTML="";
                     
                    }

                    return input;
                }
            
                function checkblank(name, error)
                        {
                            var x = document.getElementById(name).value;
                            if(x=="")
                            {
                                document.getElementById(error).innerHTML = "Please fill the required fields";
                            }
                            else{
                                document.getElementById(error).innerHTML = "";
                            }
                        }
                        
            
                        /*check validate email*/
                        function checkemail()
                        {
                            var email = document.forms["saikhant"]["txtemail"].value;
                            if(email=="")
                            {
                                document.getElementById("error_email").innerHTML = "Please fill the required email";
                            }
                            else{
                                var email = document.forms["saikhant"]["txtemail"].value;
                                var first = email.indexOf("@");
                                var second = email.lastIndexOf(".");
                                if(first<3 || second< first+3)
                                {
                                    document.getElementById("error_email").innerHTML = "Insert the email with '@' and '.' sign";
                                }
                                else{
                                    document.getElementById("error_email").innerHTML = "";
                                }
                              }
                             }
                       //checking function for textbx length
		function checklength(text,min,max)
		{
			min=min ||1;
			max=max || 100;
			if(text .length<min || text.length>max) return false;
			return true;
		}
            </script>
          
            </html>

""")




db.close()
