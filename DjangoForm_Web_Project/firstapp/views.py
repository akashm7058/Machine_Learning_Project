from django.shortcuts import render
from . MyForm import InputForm
from django.http import HttpResponse

import mysql.connector as m

# database connectivity

mydatabase=m.connect(host="localhost",user="root",password="root",database="mydb2")
query="insert into library(Student_Name,PRN_NO,Book_Issued) values(%s,%s,%s)"         #  must be "s"
cursor=mydatabase.cursor()

# Create your views here.


   
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)

def result(request):
    form = InputForm(request.POST)
    cursor.execute(query,[form['Student_Name'].value(),form['PRN_No'].value(),form['Book_Issued'].value()])     
    mydatabase.commit()
    return render(request,"welcome.html",  )


def show(request):
    query="select * from library"
    cursor.execute(query)
    l=cursor.fetchall()
    mydatabase.commit()
    return render (request,"show.html",{"records":l})

 
   


