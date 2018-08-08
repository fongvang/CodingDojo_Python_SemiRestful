from django.shortcuts import render, redirect
from .models import users

# Create your views here.
# Restful Routing (  Create | New | Index | Show | Edit | Update | Destroy  )
# CRUD Operations ( CREATE, READ, UPDATE, DESTROY )

# Index-Page (Display all Current Users)
def index(request):
    context = {"users" : users.objects.all()}
    return render(request, 'index.html', context)

# CREATE-NEW-USER (Handler Route)
def new(request):
    return render(request, "new.html")

# CREATE-NEW-USER (DB Logic and Redirect)
def add(request):
    users.objects.create(
       firstname = request.POST['firstname'],
       lastname = request.POST['lastname'],
       email = request.POST['email']
    )
    return redirect('/')

# SHOW-PAGE ROUTE HANDLER & PAGE POPULATE
def show(request, userid):
    context = {"users" : users.objects.get(id=userid)}
    return render(request, 'show.html', context)

# EDIT-PAGE ROUTE HANDLER AND DB LOGIC
def edit(request, userid):
    context = {"users" : users.objects.get(id=userid)}
    return render(request, "edit.html", context)

# UPDATE ROUTE (INDEX PAGE PASS DATA TO OVERWRITE PREVIOUS)
def update(request):
    user = users.objects.get(id=request.POST['id'])
    user.firstname = request.POST['firstname']
    user.lastname = request.POST['lastname']
    user.email = request.POST['email']
    user.save()
    return redirect('/')

# DESTROY ROUTE
def destroy(request, userid):
    userid = users.objects.get(id=userid)
    userid.delete()
    return redirect('/')






