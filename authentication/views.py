from django.db import connection
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import re

from authentication.models import LoginDetails, SignUpDetails

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    if request.method == "POST":
        email_id = request.POST['emailid']
        password = request.POST['password']
        cursor = connection.cursor()
        login_details = list(cursor.execute('''SELECT password FROM authentication_logindetails where emailid=%s''',[email_id]))
        print(login_details)
        if len(login_details) == 0:
            messages.error(request, "Email doesnot exist")
        else:
            if login_details[0][0] == password:
                return HttpResponseRedirect("/inbox")
            else:
                messages.error(request, "Incorrect password")
    return render(request, "authentication/signin.html")

def signup(request): #Register
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pno = str(request.POST['pno'])
        pword = request.POST['pword']
        cpword = request.POST['cpword']
        regex_fname = "^[A-Z]{1}[a-z]*"
        regex_lname = "^[A-Z]{1}[a-z]*"
        regex_uname = "^[a-zA-Z0-9+_.-]*"
        regex_pno = "\d{10}"
        regex_pass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        eid = uname + "@myemail.com"
        login_details = list(LoginDetails.objects.raw('SELECT * FROM authentication_logindetails'))
        same_uname = list(LoginDetails.objects.raw('SELECT * FROM authentication_logindetails where emailid=%s',[eid]))
        print(len(same_uname))
        if len(same_uname) == 0:
            if re.fullmatch(regex_fname, fname):
                if re.fullmatch(regex_lname, lname):
                    if re.fullmatch(regex_uname, uname):
                        if re.fullmatch(regex_pno, pno):
                            if pword == cpword:
                                if len(pword) >= 8:
                                    if re.fullmatch(regex_pass,pword):
                                        login_obj = LoginDetails()
                                        login_obj.uid = len(login_details)+1
                                        login_obj.emailid = uname + "@myemail.com"
                                        login_obj.password = pword
                                        login_obj.save()

                                        signup_obj = SignUpDetails()
                                        signup_obj.uid = len(login_details)+1
                                        signup_obj.first_name = fname
                                        signup_obj.last_name = lname
                                        signup_obj.username = uname
                                        signup_obj.phonenumber = pno
                                        signup_obj.password = pword
                                        signup_obj.save()

                                        return HttpResponseRedirect('/signin')
                                    else:
                                        messages.error(request, "Passwords doesnot meet the criteria")
                                else:
                                    messages.error(request, "Password length must be atleast 8")
                            else:
                                messages.error(request, "Passwords doesnot match")
                        else:
                            messages.error(request, "Invalid phone number")
                    else:
                        messages.error(request, "Invalid User name")
                else:
                    messages.error(request, "Invalid Last Name")
            else:
                messages.error(request, "Invalid First Name")
        else:
            messages.error(request,"Username already exists")

    return render(request, "authentication/register.html")

def signout(request):
    return render(request, "authentication/signout.html")

def forgot(request):
    return render(request, "authentication/forgot.html")