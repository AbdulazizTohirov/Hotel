from django.shortcuts import render,redirect

from main.models import *

def index_view(request):
    rooms = RoomsModel.objects.all()
    staffs = WorkersModel.objects.all().order_by('-id')[:4]
    context ={
        'staffs':staffs,
        'rooms':rooms,
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

def CreateBook(request):
    if request.method == 'POST':
        try:
            first_date = request.POST['name']
            last_date = request.POST['phone_number']
            email = request.POST['email']
            message = request.POST['message']
            ContactModel.objects.create(
                first_date = first_date,
                last_date = last_date,
                email = email,
                message = message,
            )
            return redirect('index_url')
        except:
            return redirect('index_url')

def Rooms1View(request):
    rooms_1 = Rooms1Model.objects.all()
    context = {
        'rooms_1': rooms_1
    }
    return render(request, 'rooms_1.html', context)

def Rooms2View(request):
    rooms_2 = Rooms2Model.objects.all()
    context = {
        'rooms_2': rooms_2
    }
    return render(request, 'rooms_2.html', context)

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













