from django.shortcuts import render,redirect
from task1.models import InsertionModel
from django.contrib import messages

def showIndex(request):
    return render(request,"writerlogin.html")


def writer_login_check(request):
    username=request.POST.get("i1")
    password = request.POST.get("i2")

    if username =="sowmya" and password=="sree":
        return render(request,"insertionpage.html")
    else:
        messages.error(request,"Invalid Login Details")
        return render(request,"writerlogin.html")


def insertion_submit(request):
    tf=request.POST.get("t1")
    title=request.POST.get("t2")
    content=request.POST.get("t3")
    image=request.FILES["t4"]
    InsertionModel.objects.create(textfield=tf,title=title,content=content,image=image)
    messages.success(request,"Inserted")
    return render(request,"insertionpage.html")


def viewIndex(request):
    return render(request, "viewerlogin.html")


def viewer_login_check(request):
    un = request.POST.get("v1")
    up = request.POST.get("v2")

    if un == "sowmya" and up == "sree":
        data=InsertionModel.objects.all()
        return render(request, "viewerpage.html",{"data":data})
    else:
        messages.error(request,"Invalid Login details")
        return render(request, "viewerlogin.html")
