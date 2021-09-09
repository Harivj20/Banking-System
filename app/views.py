from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.urls.conf import path
from .models import Account, After
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        #username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        bank_id=request.POST.get('bank_id')
        balance=request.POST.get('balance')

        if Account.objects.filter(name=name).exists():
            messages.info(request,'Username already exists!')
        elif Account.objects.filter(email=email).exists():
            messages.warning(request,'Email id already taken!')
        elif Account.objects.filter(bank_id=bank_id).exists():
            messages.warning(request,'Bank id already taken!')    
        else:
           # user=Account.objects.create(name=name,email=email,bank_id=bank_id,balance=balance)
            user=Account()
            user.name=name
            user.email=email
            user.bank_id=bank_id
            user.balance=balance
            user.save()
            messages.success(request,'Your Account is Created Successfully.')
            return redirect('/home')
    return render(request,'registration.html')            

def Transaction(request):
    transactions=After.objects.all()
    return render(request,'transaction.html',{'transactions':transactions})    

def Customers(request):
    customer=Account.objects.all()
    context={'customer':customer}
    return render(request,'customers.html',context)    

def Transfer(request):
    if request.method=='GET':
        email_avail=Account.objects.values('email')
        context={'email_avail':email_avail}
        return render(request,'transfer.html',context)
    elif request.method=='POST':
        sender_mail=request.POST.get('sender_mail')
        receiver_mail=request.POST.get('receiver_mail')
        amt=request.POST.get('amount')
        sender_amount=Account.objects.get(email=sender_mail).balance
        print(sender_mail,receiver_mail)
        receiver_amount=Account.objects.get(email=receiver_mail).balance    

        if int(sender_amount)>=int(amt):
            new_sender_amount=int(sender_amount)-int(amt)
            new_receiver_amount=int(sender_amount)+int(amt)
            sender_instance=Account.objects.filter(email=sender_mail).update(balance=new_sender_amount)
            receiver_instance=Account.objects.filter(email=receiver_mail).update(balance=new_receiver_amount)
            after_transfer=After(sender=sender_mail,receiver=receiver_mail,amount=amt)
            after_transfer.save()
            messages.info(request,'Your transaction was completed successfully!!')

            #print(after_transfer.__dict__)
            return redirect('/transfer')
           
        else:
            messages.info(request,'Sorry you didn`t have sufficient balance!!')

def Contact(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        Query=request.POST.get('Query')
        phone=request.POST.get('Phone')
        send_mail(
            Subject,
            Query,phone,
            Email,
            ['djangot1798@gmail.com'],
            fail_silently=False
        )
        messages.success(request,'Your Form is Submitted Successfully...We will get back to you inshort!!')
    return render(request,'contact.html')    

def About(request):
    return render(request,'about.html')
