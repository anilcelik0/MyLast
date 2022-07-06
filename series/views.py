from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from series.models import seriess

# Create your views here.

def index(request):    
    # with open("series/dizi.json") as fl:
    #     datas=json.load(fl)
            
    # liste = ["name","creater","kind","actor","img_url","start_time","content"]
    # for data in datas:
    #     a=0
        
    #     while a<7:
    #         dat= data[str(liste[a])]
    #         if dat is None:
    #             dat = "bulunamadı"
    #         try:
    #             dat=dat.replace("\n","")
    #             data[str(liste[a])] = dat
    #         except:
    #             data[str(liste[a])] = dat
    #         a+=1
            
    #     seriess.objects.create(name=data[str(liste[0])],creater=data[str(liste[1])],type=data[str(liste[2])],actor=data[str(liste[3])],img_url=data[str(liste[4])],start_time=data[str(liste[5])],content=data[str(liste[6])])

    # seriesss= seriess.objects.all()
    # for series in seriesss:
    #     b=series.img_url
    #     a="series/"+str(b)
    #     series.img_url=a
    #     series.save()
    
    if "term" in request.GET:
        seeriess_name=seriess.objects.filter(name__icontains=request.GET.get('term'))
        seriesss_creater=seriess.objects.filter(creater__icontains=request.GET.get('term'))
        seriesss_actor=seriess.objects.filter(actor__icontains=request.GET.get('term'))
   
        names=list()
        edited_names=list()
        for series in seeriess_name:
            names.append(series.name)
        
        for series in seriesss_creater:
            names.append(series.name)
            
        for series in seriesss_actor:
            names.append(series.name)
        
        for name in names:
            if name not in edited_names:
                edited_names.append(name)
        
        return JsonResponse(names, safe=False)

        
    return render(request, 'series/series.html')