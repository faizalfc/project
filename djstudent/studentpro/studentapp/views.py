from django.shortcuts import render
from .models import studata1
from .models import subjects 
"""
from django.shortcuts import render
from .forms import check
def display(request):
    a=check()
    return render(request, "entry.html",{"ad":a})
def getinfo(request):
    if request.method=="POST":
       
            aname=request.POST["Name"]
            email=request.POST["Email"]
            apassword=request.POST["password"]
            if apassword=="faizal@07":
                res="LOGIN SUCCES"
                return render(request,"home.html",{"r":res})
            
      
            else:
                res="INVALID ENTRY"
                a=check
                return render(request,"entry.html",{"r":res,"ad":a})
            

"""
def loadpage(request):
    return render(request,"home.html")

def start(request):
        if request.method=="POST" :
            return render(request,"add.html")
def upd(request):
       if request.method=="POST":
        return render(request,"update.html")
def delt(request):
       if request.method=="POST":
        return render(request,"delete.html")
def std(request):
    if request.method=="POST":
        return render(request,"addstu.html")
def upmark(request):
    if request.method=="POST":
        return render(request,"updatemarks.html")
def delmark(request):
    if request.method=="POST":
        return render(request,"delmark.html")
def searchstu(request):
    if request.method=="POST":
        return render(request,"search.html")

def stuinfo(request):
    if request.method=="POST":
        try:
            sname=request.POST['sn']
            sdept=request.POST['sd']
            sage=int(request.POST['sa'])
            snumber=int(request.POST['sm'])
            semail=request.POST['se']
            si=studata1(Student_Name=sname,Student_Dept=sdept,Age=sage,Mobile=snumber,Email=semail)
            si.save()
            res="STUDENT DATA SAVED...."
            
        except:
            res="STUDENT DATA NOT SAVED..."
        return render(request,"add.html",{'r':res})


def updateinfo(request):
   if request.method=="POST":
        try:
            sname=request.POST['sn']
            snumber=int(request.POST['sm'])
            si=studata1.objects.get(Student_Name=sname)
            si.Mobile=snumber
            si.save()
            res="STUDENT DATA UPDATED...."
        except:
            res="STUDENT DATA NOT UPDATED..."
        return render(request,"update.html",{'r':res})
def deleteinfo(request):
    if request.method=="POST":
        try:
            sname=request.POST['sn']
            si=studata1.objects.get(Student_Name=sname)
            si.delete()
            res="STUDENT DATA DELETED"
        except:
            res="STUDENT DATA NOT DELETED..."
        return render(request,"delete.html",{'r':res})
def stdmarks(request):
    if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            sdmark1=int(request.POST['sm1'])
            sdmark2=int(request.POST['sm2'])
            sdmark3=int(request.POST['sm3'])
            sdmark4=int(request.POST['sm4'])
            sm=subjects(Student_Name=sdname,Mark1=sdmark1,Mark2=sdmark2,Mark3=sdmark3,Mark4=sdmark4)
            sm.save()
            res="STUDENTS MARKS ADDED....."
        except:
            res="STUDENT MARKS NOT ADDED...."
        return render(request,"addstu.html",{'r':res})
def updtmark(request):
    if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            sdmark1=int(request.POST['sm1'])
            sdmark2=int(request.POST['sm2'])
            sdmark3=int(request.POST['sm3'])
            sdmark4=int(request.POST['sm4'])
            sm=subjects.objects.get(Student_Name=sdname)
            sm.Mark1=sdmark1
            sm.Mark2=sdmark2
            sm.Mark3=sdmark3
            sm.Mark4=sdmark4
            sm.save()
            res="STUDENT MARKS UPDATED"

        except:
            res="STUDENT MARKS NOT UPDATED..."
        return render(request,"updatemarks.html",{'r':res})
def deletemark(request):
       if request.method=="POST":
        try:
            sdname=request.POST['sdn']
            sm=subjects.objects.get(Student_Name=sdname)
            sm.delete()
            res="STUDENT MARKS DELETED"
        except:
            res="STUDENT MARKS NOT DELETED..."
        return render(request,"delmark.html",{'r':res})
def serch(request):
    if request.method=="POST":
        try:
            sname=request.POST['sn']
            si=studata1.objects.get(Student_Name=sname)
            sm=subjects.objects.get(Student_Name=sname)
            total=sm.Mark1+sm.Mark2+sm.Mark3+sm.Mark4
            return render(request,"view.html",{'n':si.Student_Name,'d':si.Student_Dept,'a':si.Age,'m':si.Mobile,'e':si.Email,'m1':sm.Mark1,'m2':sm.Mark2,'m3':sm.Mark3,'m4':sm.Mark4,'t':total})
        except:
            res="INVALID ENTRY......"
            return render(request,"search.html",{'r':res})
