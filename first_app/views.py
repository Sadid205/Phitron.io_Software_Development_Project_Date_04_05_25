from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def home(request):
    response =  render(request,'home.html')
    response.set_cookie('name','rahim')
    # response.set_cookie('name','korim',max_age=5)
    response.set_cookie('name','korim',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookies(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    # data = {
    #     'name':'rahim',
    #     'age': 23,
    #     'language': 'Bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'Karim'
    return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'get_session.html',{'name':name})
    # age = request.session.get('age')
    else:
        return HttpResponse("Your session has been expired.Login again")

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')