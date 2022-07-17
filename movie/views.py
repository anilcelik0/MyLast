from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movie.models import movies, movie_shares
import json

# Create your views here.

def index(request):
        
    # with open("movie/film.json") as fl:
    #     datas=json.load(fl)
            
    # liste = ["name","director","kind","actor","img_url","time","date","content"]
    # for data in datas:
    #     a=0
        
    #     while a<8:
    #         dat= data[str(liste[a])]
    #         if dat is None:
    #             dat = "bulunamadı"
    #         try:
    #             dat=dat.replace("\n","")
    #             data[str(liste[a])] = dat
    #         except:
    #             data[str(liste[a])] = dat
    #         a+=1
            
    #     movies.objects.create(name=data[str(liste[0])],director=data[str(liste[1])],type=data[str(liste[2])],actor=data[str(liste[3])],img_url=data[str(liste[4])],time=data[str(liste[5])],date=data[str(liste[6])],content=data[str(liste[7])])

    # moviess= movies.objects.all()
    # for movie in moviess:
    #     if "movie/movie" in str(movie.img_url):
    #         b=movie.img_url
    #         a=str(b)[6:]
    #         movie.img_url=a
    #         movie.save()
    
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
    
    shares = movie_shares.objects.all()
    context = {
        "shares":shares
    }

    return render(request, 'movie/movie.html',context)


def movie_page(request,movie_name):
    movie=movies.objects.filter(name=movie_name).first()
    context = {
        'movie':movie,
    }
    return render(request, 'movie/movie_page.html',context)
