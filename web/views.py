from django.shortcuts import render,redirect,HttpResponse
from web import models
from django.views import View

class ShowView(View):
    def get(self,request):
        user_obj = models.Userinfo.objects.all().values()
        return render(request,'show.html',{'user_obj':user_obj})

def DelView(request,n):
    models.Userinfo.objects.filter(pk=n).delete()
    return redirect('show')

class AddView(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.get('hobby')
        models.Userinfo.objects.create(name=name,age=age,gender=gender,hobby=hobby)
        return redirect('show')

class UpdateView(View):
    def get(self,request,n):
        user_obj = models.Userinfo.objects.filter(pk=n)
        return render(request,'update.html',{'user_obj':user_obj})

    def post(self,request,n):
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.get('hobby')
        models.Userinfo.objects.filter(pk=n).update(name=name,age=age,gender=gender,hobby=hobby)
        return redirect('show')

