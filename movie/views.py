from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from movie.models import movies, movie_shares, movie_saves, movie_share_liked, movie_list, movie_list_content
import json

# Create your views here.

def index(request):
    if "term" in request.GET:
        moviess_name=movies.objects.filter(name__icontains=request.GET.get('term'))
        moviess_director=movies.objects.filter(director__icontains=request.GET.get('term'))
        moviess_actor=movies.objects.filter(actor__icontains=request.GET.get('term'))
   
        names=list()
        edited_names=list()
        for series in moviess_name:
            names.append(series.name)
        
        for series in moviess_director:
            names.append(series.name)
            
        for series in moviess_actor:
            names.append(series.name)
        
        for name in names:
            if name not in edited_names:
                edited_names.append(name)
        
        return JsonResponse(names, safe=False)
     
    if request.method == "POST":
        save_list=[]
        likes_list=[]
        user=request.user
        saves=movie_saves.objects.filter(user=user)
        likess=movie_share_liked.objects.filter(user=user)    
        movie_lists=movie_list.objects.filter(user=user)

        for a in likess:
            likes_list.append(a.movie_share.movie.name)
            
        for a in saves:
            save_list.append(a.movie_share.movie.name)
        
        if "heart" in request.POST:
            likes_list=[]
            movie_share=request.POST["movie_share"]
            movie_share=movie_shares.objects.get(id=movie_share)
            like = movie_share_liked.objects.filter(user=user,movie_share=movie_share)
            if len(like) == 0:
                movie_share_liked.objects.create(user=user,movie_share=movie_share)
                
            else:
                like.delete()
            
            likess=movie_share_liked.objects.filter(user=user)
            for a in likess:
                likes_list.append(a.movie_share.movie.name)
            likes=len(movie_share_liked.objects.filter(movie_share=movie_share))
            movie_share.like_count=likes
            movie_share.save()
            
        elif "save" in request.POST:
            save_list=[]
            movie_save=request.POST["movie_save"]
            movie_save=movie_shares.objects.get(id=movie_save)
            save=movie_saves.objects.filter(user=user, movie_share=movie_save)
            print(len(save))
            if len(save) == 0:
                movie_saves.objects.create(user=user, movie_share=movie_save)
                
            else:
                save.delete()
                
            saves=movie_saves.objects.filter(user=user)
            for a in saves:
                save_list.append(a.movie_share.movie.name)

        elif "movie_list" in request.POST:
            movie_liste=request.POST["movie_list"]
            movie=request.POST["movie_share"]
            movie_liste=movie_list.objects.get(id=movie_liste)
            movie=movies.objects.get(id=movie)
            if len(movie_list_content.objects.filter(movie=movie, movie_list_name=movie_liste))==0:
                movie_list_content.objects.create(movie=movie, movie_list_name=movie_liste)
    
        shares = movie_shares.objects.filter(hide=0)
        context = {
            "shares":shares,
            "likess":likes_list,
            'save_list':save_list,
            "movie_lists":movie_lists
        }

        return render(request, 'movie/movie.html',context)    
    shares = movie_shares.objects.filter(hide=0)
    context = {
        "shares":shares,
    }

    return render(request, 'movie/movie.html',context)



def movie_page(request,movie_name):
    if request.method == 'POST':
        user=request.user
        val=request.POST.get('val')
        comment=request.POST.get('comment')
        hide=request.POST.get('hide')
        movie=movies.objects.get(name=movie_name)
        if hide==True:
            hide=1
        else:
            hide=0
        movie_shares.objects.create(user=user, movie=movie, hide=hide, rate=val, comment=comment)
    
    movie=movies.objects.filter(name=movie_name).first()
    movie_share=movie_shares.objects.filter(movie=movie, hide=0)
    context = {
        'movie':movie,
        'shares':movie_share
    }
    return render(request, 'movie/movie_page.html',context)

def movie_save(request):
    if request.user.is_authenticated:
        user=request.user
        save_list=[]
        likes_list=[]
        saves=movie_saves.objects.filter(user=user)
        likess=movie_share_liked.objects.filter(user=user)
        movie_lists=movie_list.objects.filter(user=user)
        for a in likess:
            likes_list.append(a.movie_share.movie.name)
            
        for a in saves:
            save_list.append(a.movie_share.movie.name)
        
        if request.method == "POST":
            
            if "heart" in request.POST:
                likes_list=[]
                movie_share=request.POST["movie_share"]
                movie_share=movie_shares.objects.get(id=movie_share)
                like = movie_share_liked.objects.filter(user=user,movie_share=movie_share)
                if len(like) == 0:
                    movie_share_liked.objects.create(user=user,movie_share=movie_share)
                    
                else:
                    like.delete()
                
                likess=movie_share_liked.objects.filter(user=user)
                for a in likess:
                    likes_list.append(a.movie_share.movie.name)
                likes=len(movie_share_liked.objects.filter(movie_share=movie_share))
                movie_share.like_count=likes
                movie_share.save()

            elif "save" in request.POST:
                save_list=[]
                movie_save=request.POST["movie_save"]
                save=movie_saves.objects.filter(user=user, movie_share=movie_save)
                save.delete()
                    
                saves=movie_saves.objects.filter(user=user)
                for a in saves:
                    save_list.append(a.movie_share.movie.name)

            elif "movie_list" in request.POST:
                movie_liste=request.POST["movie_list"]
                movie=request.POST["movie_share"]
                movie_liste=movie_list.objects.get(id=movie_liste)
                movie=movies.objects.get(id=movie)
                if len(movie_list_content.objects.filter(movie=movie, movie_list_name=movie_liste))==0:
                    movie_list_content.objects.create(movie=movie, movie_list_name=movie_liste)

                
        
        context={
            'shares':saves,
            'likess':likes_list,
            'save_list':save_list,
            "movie_lists":movie_lists
        }
        return render(request, 'movie/movie_save.html',context)
    else:
        return redirect('movie')