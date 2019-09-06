from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from . import models
User = get_user_model()

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        emailaddress = request.POST.get('eaddress')
        password = request.POST.get('psw')
        confirm = request.POST.get('cpsw')
        print(username, emailaddress, password, confirm)
        if password == confirm:
            user = User.objects.create_user(username=username, email=emailaddress, password=password)
            user.save()
            return redirect('signin')

    return render(request, 'registration.html', {})


def signin(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            print('user does not exist')
        else:
            print('user exist')
            login(request, user)
            if user.is_staff is True:
                return redirect('admin')
            else:
                return redirect('end')
    return render(request, 'signin.html', {})


@login_required(login_url='/signin')
def end(request):
    if request.method == 'POST':
        return redirect('logout')
    return render(request, 'end.html', {})


def logout_view(request):
    logout(request)
    return redirect('signin')


def edit(request, id):
    obj = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get("uname")
        print(username)
        email = request.POST.get("email")
        obj.username = username
        obj.email = email
        obj.save()
        return redirect('admin')

    return render(request, 'edit.html', {'key': obj})



def admin_view(request):
    Obj = User.objects.all()
    # for i in Obj:
    #     print(i.username, i.id, i.email)
    if request.method == 'POST' and 'logout' in request.POST:
        return redirect('logout')

    if request.method == 'POST' and 'active' in request.POST:
        idd = request.POST.get('active')
        obj = User.objects.get(id=idd)
        if obj.is_active:
             obj.is_active = False
        else:
             obj.is_active = True
        obj.save()
    # if request.method == 'POST' and 'staff' in request.POST:
    #     idd = request.POST.get('staff')
    #     obj = User.objects.get(id=idd)
    #     obj.is_staff = True
    #     obj.save()

    if request.method == 'POST' and 'staff' in request.POST:
        idd = request.POST.get('staff')
        obj = User.objects.get(id=idd)
        if obj.is_staff:
            obj.is_staff = False
        else:
            obj.is_staff = True
        obj.save()

    if request.method == 'POST' and 'delete' in request.POST:
        print("aaaaaaaaaaaaaaaaa")
        idd = request.POST.get('delete')
        print(idd)
        user = get_user_model()
        obj=user.objects.get(id=idd)
        print(obj)
        print(obj.id,obj.username)

        obj.delete()


    return render(request, 'adminhome.html', {'key': Obj})
