from django.shortcuts import render,redirect
from .models import CRUD
# Create your views here.
def home(request):
    data=CRUD.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        phone=request.POST['phone']
        obj=CRUD()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Phone=phone
        obj.save()
        return redirect('home')
    return render(request,'home.html',{'data':data})

def updatedata(request,id):
    data=CRUD.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        phone=request.POST['phone']
        
        data.Name=name
        data.Age=age
        data.Address=address
        data.Phone=phone
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})

def deletedata(request,id):
    data=CRUD.objects.get(id=id)
    data.delete()
    return redirect('home')

   
        
    
   