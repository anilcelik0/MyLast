from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from book.models import book_list, book_list_content, books
from movie.models import movie_list, movie_list_content, movies
from series.models import series_list, series_list_content, seriess

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
                    book_list.objects.create(name="Okunacaklar",user=user)
                    book_list.objects.create(name="Okunanlar",user=user)
                    movie_list.objects.create(name="İzlenecekler",user=user)
                    movie_list.objects.create(name="İzlenenler",user=user)
                    series_list.objects.create(name="İzlenecekler",user=user)
                    series_list.objects.create(name="İzlenenler",user=user)
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

def lists(request):
    user=request.user
    
    if request.method == 'POST':
        type_name=request.POST["type_name"]
        list_name=request.POST["list_name"]
        operation=request.POST["operation"]
        
        #Listeleri gösterme ve düzenleme
        if "edit"==operation:
            if "book"==type_name:
                liste=book_list.objects.filter(user=user,name=list_name).first()
                bookss=book_list_content.objects.filter(book_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'books':bookss
                }
                return render(request,'user/book_list.html',context)
                
                
            elif "movie"==type_name:
                liste=movie_list.objects.filter(user=user,name=list_name).first()
                moviess=movie_list_content.objects.filter(movie_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'movies':moviess
                }
                return render(request,'user/movie_list.html',context)
                
            elif "series"==type_name:
                liste=series_list.objects.filter(user=user,name=list_name).first()
                seriesss=series_list_content.objects.filter(series_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'seriess':seriesss
                }
                return render(request,'user/series_list.html',context)
        
        #Liste gizliliğini değiştirme
        elif "hide" in operation:
            if "book"==type_name:
                liste=book_list.objects.filter(user=user,name=list_name).first()
                if liste.hide==0:
                    liste.hide=1
                    liste.save()
                else:
                    liste.hide=0
                    liste.save()
            
                redirect('lists')
                
            elif "movie"==type_name:
                liste=movie_list.objects.filter(user=user,name=list_name).first()
                if liste.hide==0:
                    liste.hide=1
                    liste.save()
                else:
                    liste.hide=0
                    liste.save()
            
                redirect('lists')
                
            elif "series"==type_name:
                liste=series_list.objects.filter(user=user,name=list_name).first()
                if liste.hide==0:
                    liste.hide=1
                    liste.save()
                else:
                    liste.hide=0
                    liste.save()
            
                redirect('lists')
        
        #Liste silme
        elif "trash"==operation:
            if "book"==type_name:
                liste=book_list.objects.filter(user=user,name=list_name).first().delete()
                redirect('lists')
                
            elif "movie"==type_name:
                liste=movie_list.objects.filter(user=user,name=list_name).first().delete()
                redirect('lists')
                
            elif "series"==type_name:
                liste=series_list.objects.filter(user=user,name=list_name).first().delete()
                redirect('lists')
        
        #Yeni liste oluşturma
        elif "create"==operation:
            if "book"==type_name:
                hide=request.POST.get("hide")
                book_list.objects.create(name=list_name,user=user,hide=hide)
                redirect('lists')
                
            elif "movie"==type_name:
                hide=request.POST.get("hide")
                movie_list.objects.create(name=list_name,user=user,hide=hide)
                redirect('lists')
                
            elif "series"==type_name:
                hide=request.POST.get("hide")
                series_list.objects.create(name=list_name,user=user,hide=hide)
                redirect('lists')
            
        #Listeye kitap ekleme
        elif "add"==operation:
            if "book"==type_name:
                book_name=request.POST.get("search")
                book=books.objects.filter(name=book_name).first()
                liste=book_list.objects.filter(user=user,name=list_name).first()
                book_list_content.objects.create(book=book,book_list_name=liste)
                bookss=book_list_content.objects.filter(book_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'books':bookss
                }
                return render(request,'user/book_list.html',context)
                
                
            elif "movie"==type_name:
                movie_name=request.POST.get("search")
                movie=movies.objects.filter(name=movie_name).first()
                liste=movie_list.objects.filter(user=user,name=list_name).first()
                movie_list_content.objects.create(movie=movie,movie_list_name=liste)
                moviess=movie_list_content.objects.filter(movie_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'movies':moviess
                }
                return render(request,'user/movie_list.html',context)
                
            elif "series"==type_name:
                series_name=request.POST.get("search")
                series=seriess.objects.filter(name=series_name).first()
                liste=series_list.objects.filter(user=user,name=list_name).first()
                series_list_content.objects.create(series=series,series_list_name=liste)
                seriesss=series_list_content.objects.filter(series_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'seriess':seriesss
                }
                return render(request,'user/series_list.html',context)
            
        #Listeden kitap çıkarma
        elif "remove"==operation:
            if "book"==type_name:
                book_name=request.POST['book_name']
                book=books.objects.filter(name=book_name).first()
                liste=book_list.objects.filter(user=user,name=list_name).first()
                book_list_content.objects.filter(book=book,book_list_name=liste).first().delete()
                bookss=book_list_content.objects.filter(book_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'books':bookss
                }
                return render(request,'user/book_list.html',context)
                
                
            elif "movie"==type_name:
                movie_name=request.POST['movie_name']
                movie=movies.objects.filter(name=movie_name).first()
                liste=movie_list.objects.filter(user=user,name=list_name).first()
                movie_list_content.objects.filter(movie=movie,movie_list_name=liste).first().delete()
                moviess=movie_list_content.objects.filter(movie_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'movies':moviess
                }
                return render(request,'user/movie_list.html',context)
                
            elif "series"==type_name:
                series_name=request.POST['series_name']
                series=seriess.objects.filter(name=series_name).first()
                liste=series_list.objects.filter(user=user,name=list_name).first()
                series_list_content.objects.filter(series=series,series_list_name=liste).first().delete()
                seriesss=series_list_content.objects.filter(series_list_name_id=liste.id)
                
                context={
                    'liste':liste,
                    'seriess':seriesss
                }
                return render(request,'user/series_list.html',context)
            

    
    book_lists=book_list.objects.filter(user=user)
    movie_lists=movie_list.objects.filter(user=user)
    series_lists=series_list.objects.filter(user=user)
        
    context = {
        'book_lists':book_lists,
        'movie_lists':movie_lists,
        'series_lists':series_lists
    }
    return render(request,'user/lists.html',context)