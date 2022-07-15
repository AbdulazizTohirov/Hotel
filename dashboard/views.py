from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import User

def index_view(request):
    staff_quantity = WorkersModel.objects.all().count()
    request_quantity = ContactModel.objects.all().count()
    users_quantity = User.objects.all().count
    requests = ContactModel.objects.all()[:5]
    context = {
        'staff_quantity':staff_quantity,
        'request_quantity':request_quantity,
        'users_quantity':users_quantity,
        'requests':requests
    }
    return render (request, 'dashboard/index.html',context)

def worker_create(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            status = request.POST['status']
            img = request.FILES['img']
            WorkersModel.objects.create(

            name = name,
            status =status,
            img = img,
        )
        except:
            return HttpResponse('Xatolik')
        
    return redirect('workers_url')

def workers(request):
    workers = WorkersModel.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/workers.html', context)

def requests(request):
    requests = ContactModel.objects.all()
    context = {
        'requests': requests
    }
    return render(request, 'dashboard/teachers.html', context)

def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/teachers.html', context)

def rooms(request):
    rooms = RoomsModel.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms.html', context)
