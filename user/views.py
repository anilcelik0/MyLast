from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from book.models import book_list, book_list_content, books, book_shares, book_share_liked, book_saves
from movie.models import movie_list, movie_list_content, movies, movie_shares, movie_share_liked, movie_saves
from series.models import series_list, series_list_content, seriess, series_shares, series_share_liked, series_saves
from user.models import follow_event

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
    if request.user.is_authenticated:
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
    else:
        redirect('book')

def profile(request):
    if request.user.is_authenticated:
        user=request.user
        followers=follow_event.objects.filter(followed_user=user)
        followers_len=len(followers)
        book_share=book_shares.objects.filter(user=user)
        movie_share=movie_shares.objects.filter(user=user)
        series_share=series_shares.objects.filter(user=user)
        
        context={
            'user':user,
            'followers':followers,
            'followers_len':followers_len,
            'book_share':book_share,
            'movie_share':movie_share,
            'series_share':series_share
        }
        return render(request, 'user/profile.html',context)
    else:
        return redirect('book')

def settings(request):
    if request.user.is_authenticated:
        user=request.user
        followers=follow_event.objects.filter(followed_user=user)
        followers_len=len(followers)
        
        if request.method == 'POST':
            #öğe al
            if 'send' in request.POST:
                name = request.POST['name']
                surname = request.POST['surname']
                sendingusername = request.POST['username']
                email = request.POST['email']

                user = request.user

                if user.username != sendingusername:
                    if User.objects.filter(username = sendingusername).exists():
                        messages.add_message(request,messages.WARNING,'Bu kullanıcı adı kullanılmakta. Başka bir kullanıcı adı girmeyi deneyin')
                        return redirect('settings')

                    else:
                        if user.email != email:
                        
                            if User.objects.filter(email = email).exists():
                                messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                                return redirect('settings')

                            else:
                                User.objects.filter(username = user.username).update(first_name = name,last_name = surname, username = sendingusername, email = email)
                                messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                                return redirect('settings')
                        else:
                            User.objects.filter(username = user.username).update(first_name = name,last_name = surname, username = sendingusername)

                            messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                            return redirect('settings')


                else:
                    if user.email != email:
                    
                        if User.objects.filter(email = email).exists():
                            messages.add_message(request,messages.WARNING,'Bu email kullanılmakta. Başka bir email girmeyi deneyin')
                            return redirect('settings')

                        else:
                            User.objects.filter(username = user.username).update(first_name = name,last_name = surname, email = email)
                            messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                            return redirect('settings')

                    else:
                        User.objects.filter(username = user.username).update(first_name = name, last_name = surname)
                        messages.add_message(request,messages.SUCCESS,'kullanıcı başarıyla güncllendi')
                        return redirect('settings')


            elif 'pswsend' in request.POST:
                oldpassword = request.POST['oldpassword']
                password = request.POST['password']
                repassword = request.POST['repassword']

                user = request.user 


                if user.check_password(oldpassword):
                    if password == repassword:
                        user.set_password(password)
                        messages.add_message(request,messages.SUCCESS,'Şifreniz güncellenmiştir')
                        return redirect('settings')

                    else:
                        messages.add_message(request,messages.WARNING,'Şifreniz uyuşmuyor')
                        return redirect('settings')
                else:
                    messages.add_message(request,messages.WARNING,'Şifrenizi yalnış girdiniz')
                    return redirect('settings')

        
        context={
            'user':user,
            'followers':followers,
            'followers_len':followers_len,
        }
        return render(request, 'user/settings.html',context)
    else:
        return redirect('book')

def profiles(request, username):
    search_user=User.objects.get(username=username)
    book_sharess=book_shares.objects.filter(user=search_user, hide=0)
    movie_sharess=movie_shares.objects.filter(user=search_user, hide=0)
    series_sharess=series_shares.objects.filter(user=search_user, hide=0)
    
        
    if request.method == "POST":
        user=request.user
        #like list
        book_likes_list=[]
        movie_likes_list=[]
        series_likes_list=[]
        likess=book_share_liked.objects.filter(user=user)
        for a in likess:
            book_likes_list.append(a.book_share.book.name)
            
        likess=movie_share_liked.objects.filter(user=user)
        for a in likess:
            movie_likes_list.append(a.movie_share.movie.name)
            
        likess=series_share_liked.objects.filter(user=user)
        for a in likess:
            series_likes_list.append(a.series_share.series.name)
            
        #save lists
        book_save_list=[]
        movie_save_list=[]
        series_save_list=[]
        
        saves=book_saves.objects.filter(user=user)
        for a in saves:
            book_save_list.append(a.book_share.book.name)
            
        saves=movie_saves.objects.filter(user=user)
        for a in saves:
            movie_save_list.append(a.movie_share.movie.name)
            
        saves=series_saves.objects.filter(user=user)
        for a in saves:
            series_save_list.append(a.series_share.series.name)
            
        #lists
        book_lists=book_list.objects.filter(user=user)
        movie_lists=movie_list.objects.filter(user=user)
        series_lists=series_list.objects.filter(user=user)

        
        if "heart" in request.POST:
            if "book_share" in request.POST:
                book_likes_list=[]
                book_share=request.POST["book_share"]
                book_share=book_shares.objects.get(id=book_share)
                like = book_share_liked.objects.filter(user=user,book_share=book_share)
                if len(like) == 0:
                    book_share_liked.objects.create(user=user,book_share=book_share)
                    
                else:
                    like.delete()
                
                likess=book_share_liked.objects.filter(user=user)
                for a in likess:
                    book_likes_list.append(a.book_share.book.name)
                likes=len(book_share_liked.objects.filter(book_share=book_share))
                book_share.like_count=likes
                book_share.save()
                
            elif "movie_share" in request.POST:
                movie_likes_list=[]
                movie_share=request.POST["movie_share"]
                movie_share=movie_shares.objects.get(id=movie_share)
                like = movie_share_liked.objects.filter(user=user,movie_share=movie_share)
                if len(like) == 0:
                    movie_share_liked.objects.create(user=user,movie_share=movie_share)
                    
                else:
                    like.delete()
                
                likess=movie_share_liked.objects.filter(user=user)
                for a in likess:
                    movie_likes_list.append(a.movie_share.movie.name)
                likes=len(movie_share_liked.objects.filter(movie_share=movie_share))
                movie_share.like_count=likes
                movie_share.save()

            if "series_share" in request.POST:
                series_likes_list=[]
                series_share=request.POST["series_share"]
                series_share=series_shares.objects.get(id=series_share)
                like = series_share_liked.objects.filter(user=user,series_share=series_share)
                if len(like) == 0:
                    series_share_liked.objects.create(user=user,series_share=series_share)
                    
                else:
                    like.delete()
                
                likess=series_share_liked.objects.filter(user=user)
                for a in likess:
                    series_likes_list.append(a.series_share.series.name)
                likes=len(series_share_liked.objects.filter(series_share=series_share))
                series_share.like_count=likes
                series_share.save()
                
        elif "save" in request.POST:
            if "book_save" in request.POST:
                book_save_list=[]
                book_save=request.POST["book_save"]
                book_save=book_shares.objects.get(id=book_save)
                save=book_saves.objects.filter(user=user, book_share=book_save)
                if len(save) == 0:
                    book_saves.objects.create(user=user, book_share=book_save)
                    
                else:
                    save.delete()
                    
                saves=book_saves.objects.filter(user=user)
                for a in saves:
                    book_save_list.append(a.book_share.book.name)
                    
            if "movie_save" in request.POST:
                movie_save_list=[]
                movie_save=request.POST["movie_save"]
                movie_save=movie_shares.objects.get(id=movie_save)
                save=movie_saves.objects.filter(user=user, movie_share=movie_save)
                if len(save) == 0:
                    movie_saves.objects.create(user=user, movie_share=movie_save)
                    
                else:
                    save.delete()
                    
                saves=movie_saves.objects.filter(user=user)
                for a in saves:
                    movie_save_list.append(a.movie_share.movie.name)
                    
            if "series_save" in request.POST:
                series_save_list=[]
                series_save=request.POST["series_save"]
                series_save=series_shares.objects.get(id=series_save)
                save=series_saves.objects.filter(user=user, series_share=series_save)
                if len(save) == 0:
                    series_saves.objects.create(user=user, series_share=series_save)
                    
                else:
                    save.delete()
                    
                saves=series_saves.objects.filter(user=user)
                for a in saves:
                    series_save_list.append(a.series_share.series.name)

        elif "list" in request.POST:
            if "book_list" in request.POST:
                book_liste=request.POST["book_list"]
                book=request.POST["book_share"]
                book_liste=book_list.objects.get(id=book_liste)
                book=books.objects.get(id=book)
                if len(book_list_content.objects.filter(book=book, book_list_name=book_liste))==0:
                    book_list_content.objects.create(book=book, book_list_name=book_liste)
 
            elif "movie_list" in request.POST:
                movie_liste=request.POST["movie_list"]
                movie=request.POST["movie_share"]
                movie_liste=movie_list.objects.get(id=movie_liste)
                movie=movies.objects.get(id=movie)
                if len(movie_list_content.objects.filter(movie=movie, movie_list_name=movie_liste))==0:
                    movie_list_content.objects.create(movie=movie, movie_list_name=movie_liste)

            elif "series_list" in request.POST:
                series_liste=request.POST["series_list"]
                series=request.POST["series_share"]
                series_liste=series_list.objects.get(id=series_liste)
                series=seriess.objects.get(id=series)
                if len(series_list_content.objects.filter(series=series, series_list_name=series_liste))==0:
                    series_list_content.objects.create(series=series, series_list_name=series_liste)


        context={
            'search_user':search_user,
            'book_share':book_sharess,
            'movie_share':movie_sharess,
            'series_share':series_sharess,
            'book_like_list':book_likes_list,
            'movie_like_list':movie_likes_list,
            'series_like_list':series_likes_list,
            'book_save_list':book_save_list,
            'movie_save_list':movie_save_list,
            'series_save_list':series_save_list,
            "book_lists":book_lists,
            "movie_lists":movie_lists,
            "series_lists":series_lists
        }

        return render(request, 'user/profiles.html', context)    
    context={
        'search_user':search_user,
        'book_share':book_sharess,
        'movie_share':movie_sharess,
        'series_share':series_sharess,
    }

    return render(request, 'user/profiles.html', context)