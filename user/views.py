from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        # fakepp = 'fakepp.jpg'
        #öğeleri al
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        
        #kontrol

        if password == repassword:
            
            if User.objects.filter(username = username).exists():
                messages.add_message(request,messages.WARNING,'Bu kullanıcı adı kullanılmakta. Başka bir kullanıcı adı girmeyi deneyin')
                return redirect('book')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                    return redirect('book')

                else:
                    #kayıt
                    user = User.objects.create_user(first_name = name,last_name = surname, username = username, password = password, email = email)
                    user.save()
                    # pp = ppUser.objects.create(username = username, pp = fakepp)
                    # pp.save()
                    messages.add_message(request,messages.SUCCESS,'Kullanıcı başarı ile oluşturuldu')
                    return redirect('book')
        else:
            messages.add_message(request, messages.WARNING, 'Parolalar uyuşmuyor')
            return redirect('book')
    
    
    
    else:
        return render(request, 'book/book.html')


def login(request):
        #öğeleri al
    username = request.POST['username']
    password = request.POST['password']
    
    #kontrol
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)

        messages.add_message(request, messages.SUCCESS, 'Oturum açıldı')
        return redirect('book')

    else:
        messages.add_message(request, messages.ERROR, 'Kullanıcı adı veya parola hatalı')
        return redirect('book')


def logout(request):
    
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'Oturum kapatıldı')

    return redirect('book')
