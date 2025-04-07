from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,AddRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Records

# ------- home page---------
def home(request):
    return render(request, 'webapp/index.html')

# ------- Register--------
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('login')
    context = {
        'form': form
    }        
    return render(request,'webapp/register.html',context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request,"You're logged-in successfully!")
                return redirect('dashboard')
            else:
                messages.error(request, "Oops! Invalid username or password! Try Again!")
    context={
        "form":form
    }
    return render(request,'webapp/login.html',context)

def logout(request):
    auth.logout(request)
    messages.success(request,"You're logged-out successfully!")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request): 
    all_records = Records.objects.filter(user=request.user)
    context = {'records': all_records}

    return render(request, 'webapp/dashboard.html',context)

@login_required(login_url='login')
def create_record(request): 
    form = AddRecordForm()
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user  # 🔑 Link record to the logged-in user
            record.save()
            messages.success(request, "Record Created!")
            return redirect('dashboard')
        else:
            messages.error(request, "Sorry! Can't create the record. Try again!")
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)

@login_required(login_url='login')
def update_record(request,pk): 
    record = Records.objects.get(id = pk,user=request.user)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record )
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated!")
            return redirect('dashboard')
        else:
            messages.error(request,"Sorry! Can't Update a record! Try again!")
    context = {'form':form}
    return render(request, 'webapp/update-record.html',context)


@login_required(login_url='login')
def view_record(request,pk): 
    my_record = Records.objects.get(id = pk,user = request.user)

    return render(request, 'webapp/view-record.html', {'record': my_record})

@login_required(login_url='login') 
def delete_record(request,pk): 
    record = Records.objects.get(id=pk,user = request.user)
    record.delete()
    messages.success(request,"Record Deleted!")
    return redirect('dashboard')