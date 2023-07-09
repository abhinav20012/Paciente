from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from home.models import signUpInfo1, signUpInfo2
import hashlib
from django.core.mail import send_mail
import random

sign_up_info1 = []
otp = '****'
req = None

# Create your views here.
def index(request):
    context = {
        'variable_name' : 'value'
    }
    if request.user.is_authenticated:
        return render(request, 'index.html', context)

def signup1(request):
    return render(request, 'signup1.html')

def signup2(request):
    global sign_up_info1
    global otp
    if request.method == "POST":
        email = request.POST.get('loginUser')
        password = request.POST.get('loginPassword')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            raise Exception
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        sign_up_info1 = signUpInfo1(loginUser = email, loginPassword = hashed_password)
        sign_up_info1.save()  # TBD

        otp = str(random.randint(1000, 9999))
        send_mail(
        'Paciente: Email Verification',
        otp,
        'paciente.inc@yahoo.com',
        [email],
        fail_silently = False,
        )

    return render(request, 'signup2.html')

def login(request):
    global sign_up_info1
    global otp
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        enteredOTP = request.POST.get('otp')
        document = request.POST.get('document')
        if otp != enteredOTP:
            raise Exception
        sign_up_info2 = signUpInfo2(firstName = firstname, lastName = lastname, email = email, otp = enteredOTP, document = document)
        sign_up_info2.save()
    # return render(request, 'index.html')
    return HttpResponseRedirect('/login/')

def redirectToHome(request):
    global req
    req = request
    return HttpResponseRedirect('/home/')

def home(request):
    global req
    if req == None:
        return render(request, 'home.html')    
    request = req
    if signUpInfo1.objects.filter(loginUser = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0:
        raise Exception("Access Denied by Paciente")
    req = None
    return render(request, 'home.html')

def doctor(request):
    return render(request, 'doctor.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("services.html")