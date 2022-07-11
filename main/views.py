from django.shortcuts import render,redirect

from main.models import *

def index_view(request):
    rooms = RoomsModel.objects.all()
    blogs = WorkersModel.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request, 'index.html',context)

def CreateContact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            message = request.POST['message']
            ContactModel.objects.create(
                name = name,
                phone_number = phone_number,
                email = email,
                message = message,
            )
            return redirect('index_url')
        except:
            return redirect('index_url')

def ContactView(request):
    return render (request, 'contact.html')

def BooknowView(request):
    return render (request, 'booknow.html')

def RoomsView(request):
    return render (request, 'rooms.html')
    
def BlogView(request):
    return render (request, 'blog.html')
    
def AboutView(request):
    return render (request, 'about.html')

def StaffView(request):
    return render (request, 'staff.html')


def Contact2View(request):
    return render (request, 'contact_2.html')













