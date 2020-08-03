import json
from email import message

import requests
from django.http import HttpResponseRedirect, request,HttpResponse
from django.views.generic import ListView, View
from .models import Basicinfo, Tourism, scholars_list, VisaInformation, CountryImages, Contacts, newScholarship, reviews
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage





def index(request):
    template_name = 'mysite/single_post.html'
    if request.method == 'POST':
        country = request.POST['country']
        type = request.POST['type']


        if type == 'study_visa':
            obj = Basicinfo.objects.get(name=country)
            obj2 = VisaInformation.objects.get(name=country)
            obj3 = CountryImages.objects.get(Country=country)

            context = {
                'Country': obj.name,
                'PASSPORT': obj.validity,
                'BLANK': obj.blank_pages,
                'VACCINATIONS': obj.vaccination,
                'CURRENCY': obj.amount_entry,
                'CURRENCYE': obj.amount_exit,
                'study': obj2.study_visa,
                'image': obj3.Country_photo,
                'link': obj.link
            }
            return render(request, 'mysite/study.html', {'context': context})

        elif type == 'visit_visa':
            obj = Basicinfo.objects.get(name=country)
            obj2 = VisaInformation.objects.get(name=country)
            obj3 = CountryImages.objects.get(Country=country)

            context = {
                'Country': obj.name,
                'PASSPORT': obj.validity,
                'BLANK': obj.blank_pages,
                'VACCINATIONS': obj.vaccination,
                'CURRENCY': obj.amount_entry,
                'CURRENCYE': obj.amount_exit,
                'Tourism': obj2.visit_visa,
                'image': obj3.Country_photo,
                'link': obj.link
            }
            return render(request, 'mysite/tourism.html', {'context':context})

        elif type == 'employment_visa':
            obj = Basicinfo.objects.get(name=country)
            obj2 = VisaInformation.objects.get(name=country)
            obj3 = CountryImages.objects.get(Country=country)

            context = {
                'Country': obj.name,
                'PASSPORT': obj.validity,
                'BLANK': obj.blank_pages,
                'VACCINATIONS': obj.vaccination,
                'CURRENCY': obj.amount_entry,
                'CURRENCYE': obj.amount_exit,
                'employment': obj2.employment_visa,
                'image': obj3.Country_photo,
                'link' : obj.link
            }
            return render(request, 'mysite/Employment.html', {'context':context})
        elif type == 'business_visa':
            obj = Basicinfo.objects.get(name=country)
            obj2 = VisaInformation.objects.get(name=country)
            obj3 = CountryImages.objects.get(Country=country)

            context = {
                'Country': obj.name,
                'PASSPORT': obj.validity,
                'BLANK': obj.blank_pages,
                'VACCINATIONS': obj.vaccination,
                'CURRENCY': obj.amount_entry,
                'CURRENCYE': obj.amount_exit,
                'business': obj2.business_visa,
                'image': obj3.Country_photo,
                'link': obj.link
            }
            return render(request, 'mysite/Bussines.html', {'context':context})




    else:
        Norway = scholars_list.objects.filter(Country='Norway')
        Germany = scholars_list.objects.filter(Country='Germany')
        America = scholars_list.objects.filter(Country='America')
        Spain = scholars_list.objects.filter(Country='Spain')


        context = {
            'Norway': Norway,
            'Germany': Germany,
            'America': America,
            'Spain': Spain

            }
        return render(request, 'mysite/index.html', {'context': context}, )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index.html')

        else:
            p = 'Invalid Credentials OR Activate your Email Address!'
            return render(request, 'mysite/login.html', {'alert_flag': p})
    else:
        return render(request, 'mysite/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index.html')


def signup(request):
    if request.method == 'POST':
        Email = request.POST['email']
        Username = request.POST['user']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if Username == "" or Email == "" or pass1 == "" or pass2 == "" or fname == "" or lname == "":
            p = 'Incomplete Credentials!'
            return render(request, 'mysite/signup.html', {'alert_flag': p})

        if pass1 == pass2:
            if User.objects.filter(username=Username).exists():
                p = 'UserName Already Exist.Try with another one!'
                return render(request, 'mysite/signup.html', {'alert_flag': p})

            elif User.objects.filter(email=Email).exists():
                p = 'User Already Exist!'
                return render(request, 'mysite/signup.html', {'alert_flag': p})
            else:

                user = User.objects.create_user(first_name=fname,last_name=lname,email=Email, password=pass1, username=Username)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Email verification'
                message = render_to_string('mysite/acc_activate_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                to_email = Email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
                # p = 'User Created Successfully!'
                # return render(request, 'mysite/login.html', {'alert_flag': p})
        else:
            p = 'Password does not match!'
            return render(request, 'mysite/signup.html', {'alert_flag': p})
    else:
        return render(request, 'mysite/signup.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # auth.login(request, user)
        # return redirect('index.html')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



def about(request):
    if request.method == 'POST':
        review = request.POST['review']
        if review == '':
            error = 'Write something'
            return render(request, 'mysite/about.html', {'error': error})
        else:
            add = reviews.objects.create(username=request.user.username, comment=review)
            add.save()
            context = reviews.objects.all()
            return render(request, 'mysite/about.html', {'context': context})
    else:
        context = reviews.objects.all()
        return render(request, 'mysite/about.html', {'context': context})

def passwordConfirm(request):
    if request.method == 'POST':
        newpass = request.POST['pass1']
        newpass2 =  request.POST['pass2']

        if newpass == newpass2:
            user = User.objects.get(email=var)
            user.set_password(newpass)
            user.save()
            p = 'Your password is reset successfully!'
            return render(request, 'mysite/login.html', {'alert_flag': p})
        else:
            p = 'Password do not match!'
            return render(request, 'mysite/resetPassword.html', {'alert_flag': p})


    else:
        print(var)
        return render(request, 'mysite/passwordConfirm.html')

def resetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            global var
            var = email
            print(var)
            mail_subject = 'Password Reset'
            message = 'Hi!,' \
                      'Please click on the link to reset your password' \
                      'http://127.0.0.1:8000/passwordConfirm.html'
            to_email = email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to reset you password')

        else:
            p = 'There is no account on this email address!'
            return render(request, 'mysite/resetPassword.html', {'alert_flag': p})

    else:
        return render(request, 'mysite/resetPassword.html')




class scholars_List(ListView):
    template_name = 'mysite/scholars_List.html'

    def get_queryset(self):
        relation = self.request.GET.get('country', None)
        if relation == 'Norway':
            return scholars_list.objects.filter(Country='Norway')
        elif relation == 'Germany':
            return scholars_list.objects.filter(Country='Germany')
        elif relation == 'Spain':
            return scholars_list.objects.filter(Country='Spain')
        elif relation == 'Canada':
            return scholars_list.objects.filter(Country='Canada')
        elif relation == 'Australia':
            return scholars_list.objects.filter(Country='Australia')
        elif relation == 'Italy':
            return scholars_list.objects.filter(Country='Italy')
        elif relation == 'Japan':
            return scholars_list.objects.filter(Country='Japan')
        elif relation == 'China':
            return scholars_list.objects.filter(Country='China')
        elif relation == 'UnitedKingdom':
            return scholars_list.objects.filter(Country='UnitedKingdom')
        elif relation == 'Bachelor':
            return scholars_list.objects.filter(level='Bachelor')
        elif relation == 'Master':
            return scholars_list.objects.filter(level='Master')
        elif relation == 'PHD':
            return scholars_list.objects.filter(level='PHD')





def tourism(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Basicinfo.objects.filter(name=srch)
            if match:
                obj = Basicinfo.objects.get(name=srch)
                obj2 = VisaInformation.objects.get(name=srch)
                obj3 = CountryImages.objects.get(Country=srch)

                context = {
                    'Country': obj.name,
                    'PASSPORT': obj.validity,
                    'BLANK': obj.blank_pages,
                    'VACCINATIONS': obj.vaccination,
                    'CURRENCY': obj.amount_entry,
                    'CURRENCYE': obj.amount_exit,
                    'Tourism': obj2.visit_visa,
                    'image': obj3.Country_photo,
                    'link' : obj.link
                }
                return render(request, 'mysite/tourism.html', {'context': context})
            else:
                return HttpResponseRedirect('mysite/tourism.html')
        else:
            return render(request, 'mysite/tourism.html')

    return render(request, 'mysite/tourism.html')

def bussines(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Basicinfo.objects.filter(name=srch)
            if match:
                obj = Basicinfo.objects.get(name=srch)
                obj2 = VisaInformation.objects.get(name=srch)
                obj3 = CountryImages.objects.get(Country=srch)

                context = {
                    'Country': obj.name,
                    'PASSPORT': obj.validity,
                    'BLANK': obj.blank_pages,
                    'VACCINATIONS': obj.vaccination,
                    'CURRENCY': obj.amount_entry,
                    'CURRENCYE': obj.amount_exit,
                    'business': obj2.business_visa,
                    'image': obj3.Country_photo,
                    'link': obj.link

                }
                return render(request, 'mysite/Bussines.html', {'context': context})
            else:
                return HttpResponseRedirect('mysite/Bussines.html')
        else:
            return render(request, 'mysite/Bussines.html')

    return render(request, 'mysite/Bussines.html')


def employment(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Basicinfo.objects.filter(name=srch)
            if match:
                obj = Basicinfo.objects.get(name=srch)
                obj2 = VisaInformation.objects.get(name=srch)
                obj3 = CountryImages.objects.get(Country=srch)

                context = {
                    'Country': obj.name,
                    'PASSPORT': obj.validity,
                    'BLANK': obj.blank_pages,
                    'VACCINATIONS': obj.vaccination,
                    'CURRENCY': obj.amount_entry,
                    'CURRENCYE': obj.amount_exit,
                    'employment': obj2.employment_visa,
                    'image': obj3.Country_photo,
                    'link': obj.link
                }
                return render(request, 'mysite/Employment.html', {'context': context})
            else:
                return HttpResponseRedirect('mysite/Employment.html')
        else:
            return render(request, 'mysite/Employment.html')

    return render(request, 'mysite/Employment.html')

def study(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Basicinfo.objects.filter(name=srch)
            if match:
                obj = Basicinfo.objects.get(name=srch)
                obj2 = VisaInformation.objects.get(name=srch)
                obj3 = CountryImages.objects.get(Country=srch)

                context = {
                    'Country': obj.name,
                    'PASSPORT': obj.validity,
                    'BLANK': obj.blank_pages,
                    'VACCINATIONS': obj.vaccination,
                    'CURRENCY': obj.amount_entry,
                    'CURRENCYE': obj.amount_exit,
                    'study': obj2.study_visa,
                    'image': obj3.Country_photo,
                    'link': obj.link
                }
                return render(request, 'mysite/Study.html', {'context': context})
            else:
                return HttpResponseRedirect('mysite/Study.html')
        else:
            return render(request, 'mysite/Study.html')

    return render(request, 'mysite/Study.html')

def Contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            subject = request.POST['subject']
            message = request.POST['message']

            if firstname == "" or lastname == ""  or subject == "" or message == "":
                info = 'Incomplete Information!'
                return render(request, 'mysite/contact.html', {'info': info})
            else:
                cont = Contacts.objects.create(firstname=firstname, lastname=lastname, email=request.user.email, subjects=subject, message=message)
                cont.save
                info = 'Message sent successfully.!'
                return render(request, 'mysite/contact.html', {'info': info})
        else:

            info = 'First you have to login...'
            return render(request, 'mysite/contact.html', {'info':info})


    else:
        return render(request, 'mysite/contact.html')

def Detail(request):
    return render(request, 'mysite/Detail.html')

def PostScholarship(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            country = request.POST['country']
            name = request.POST['name']
            desription = request.POST['description']
            level =request.POST['level']
            last = request.POST['last']
            link = request.POST['link']
            amount = request.POST['amount']

            if country == "" or name == "" or desription == "" or last == "" or link == "":
                aler_flag = 'Incomplete Form'
                return render(request, 'mysite/PostScholarship.html', {'aler_flag':aler_flag})
            elif scholars_list.objects.filter(Name=name):
                aler_flag = 'Already Exits'
                return render(request, 'mysite/PostScholarship.html', {'aler_flag': aler_flag})
            else:
                add = scholars_list.objects.create(Country=country, Name=name, Description=desription, last_date=last,
                                                   link=link, scholarship=amount, level=level, status=0)
                new = newScholarship.objects.create(username=request.user.username, email=request.user.email, name=name)
                new.save
                add.save
                message = 'Scolarships is Added'
                return render(request, 'mysite/scholars_list.html', {'message': message})
        else:

            aler_flag = 'First you have to login...'
            return render(request, 'mysite/PostScholarship.html', {'aler_flag':aler_flag})

    else:
        return render(request, 'mysite/PostScholarship.html')


