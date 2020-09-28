from django.shortcuts import render,HttpResponseRedirect
from enroll.form import StudentRegistration
from django.views.generic.base import TemplateView,RedirectView
from .models import User
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

class add_show(TemplateView):
    # template_name="enroll/addandshow.html"
    # def get_context_data(self,*args,**kwargs):
        # context=super().get_context_data(**kwargs)
        # fm=StudentRegistration()
        # stud=User.objects.all()
        # context={'stud':stud,'form':fm}

        # return context
    
            def get(self,request,*args,**kwargs):
                    stud=User.objects.all()
                    fm=StudentRegistration()
                    return render(request,'enroll/addandshow.html',{'form':fm,'stud':stud})
            def post(self,request):
                fm=StudentRegistration(request.POST)
                if fm.is_valid():
                    nm=fm.cleaned_data['name']
                    em=fm.cleaned_data['email']
                    pw=fm.cleaned_data['password']
                    reg=User(name=nm,email=em,password=pw)
                    reg.save()
                    return HttpResponseRedirect('/addandshow/')
    
        

class delete_data(RedirectView):
    url='/addandshow/'
    def get_redirect_url(self,*args,**kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

class update_data(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':fm})

    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/addandshow/')

def user_logout(request):
    return HttpResponseRedirect('/')

def user_login(request):
        if request.method == 'POST':
            username=request.POST.get('name')
            password=request.POST.get('password')
            print(username)
            print(password)
            ti=User.objects.all()
            m=0
            for p in ti:
                print(p.name)
                print(p.password)
                if(p.name==username and p.password==password):
                    print("valid")
                    m=1
                    po=1
                
            if m==0:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            else:
                return HttpResponseRedirect("/addandshow/")
            # >>> User.objects.values('id','first_name','last_name')
            
            # user=authenticate(name=username,password=password)
            # if user:
            #     if user.is_active:
            #         login(request,user)
            #         return render(request,enroll/addandshow.html)
            #     else:
            #         return HttpResponse("ACCOUNT NOT ACTIVE")
            # else:
            
            #     return HttpResponse("INVALID LOGIN DETAILD SUPLIED!")
        else:
            return render(request,'enroll/login.html',{})
   
    