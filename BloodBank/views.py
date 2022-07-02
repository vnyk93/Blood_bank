from django.shortcuts import render , redirect

from . import models

def saverequest(request):
    id = request.session['user'][0]
    models.saveRequest(request.POST,id)
    return redirect('/user/request')

def bloodrequest(request):
    id = request.session['user'][0]    
    userrequest = models.listUserRequest(id)
    otherrequest = models.listOtherRequest(id)
    return render(request,'request.html',{
        'userrequest':userrequest,
        'otherrequest':otherrequest
    })

def userhome(request):
    name = request.session['user'][1]
    id = request.session['user'][0]
    lst = models.listUser(id)
    return render(request,'userhome.html',{
        'name':name , 'users'  :lst
    })

def logout(request):
    del request.session['user']
    return redirect('/')

#*************************************
def userlogin(request):
    data = models.loginUser(request.POST)
    if data is None:
        url = '/login?err=1'
        return redirect(url)
    else:  
        request.session['user'] = data      
        return redirect('/user/home')

def usersave(request):
    status = models.saveUser(request.POST)
    url = '/register?reg='+str(status)
    return redirect(url)

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')    

def register(request):
    msg = ""
    #print(request.GET.get('reg'))
    if request.GET.get('reg') is not None:
        if request.GET.get('reg')=='True':
            msg="Registeration Done !"
        else:
            msg="Registeration Failed !"            

    return render(request,'register.html',{
        'msg':msg
    })     

def login(request):
    msg = ""    
    if request.GET.get('err') is not None:
        msg="Login Failed !"  
    return render(request,'login.html',{
        'msg':msg
    }) 


# Cookie (Client-side) , Session (Server-side)   