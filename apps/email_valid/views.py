from django.shortcuts import render, redirect, HttpResponse
from .models import Email
# Create your views here.
def index(request):
    if not 'errors' in request.session:
        request.session['errors'] = []
    return render (request, 'email_display/index.html')

def create_email(request):
    if request.method == "POST":
        result=[]
        result = Email.email_mgr.register(request.POST['email'])
        if result[0]:
            request.session['email'] = result[1].email
            request.session.pop('errors')
            return redirect('/success')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect ('/')

def success(request):
    emails = Email.email_mgr.all()
    return render (request, 'email_display/success.html', {'emails': emails, 'your_email': request.session.get('email')})

def destroy(request, id):
    result = Email.email_mgr.destroy(id)
    return redirect('/success')
