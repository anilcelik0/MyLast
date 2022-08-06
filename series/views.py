from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import json
from series.models import seriess, series_shares, series_saves, series_share_liked,series_list, series_list_content

# Create your views here.

def index(request):    
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
    
    
    if request.method == "POST":
        save_list=[]
        likes_list=[]
        user=request.user
        saves=series_saves.objects.filter(user=user)
        likess=series_share_liked.objects.filter(user=user)
        series_lists=series_list.objects.filter(user=user)
        for a in likess:
            likes_list.append(a.series_share.series.name)
            
        for a in saves:
            save_list.append(a.series_share.series.name)
    

        if "heart" in request.POST:
            likes_list=[]
            series_share=request.POST["series_share"]
            series_share=series_shares.objects.get(id=series_share)
            like = series_share_liked.objects.filter(user=user,series_share=series_share)
            if len(like) == 0:
                series_share_liked.objects.create(user=user,series_share=series_share)
                
            else:
                like.delete()
            
            likess=series_share_liked.objects.filter(user=user)
            for a in likess:
                likes_list.append(a.series_share.series.name)
            likes=len(series_share_liked.objects.filter(series_share=series_share))
            series_share.like_count=likes
            series_share.save()

        elif "save" in request.POST:
            save_list=[]
            series_save=request.POST["series_save"]
            series_save=series_shares.objects.get(id=series_save)
            save=series_saves.objects.filter(user=user, series_share=series_save)
            print(len(save))
            if len(save) == 0:
                series_saves.objects.create(user=user, series_share=series_save)
                
            else:
                save.delete()
                
            saves=series_saves.objects.filter(user=user)
            for a in saves:
                save_list.append(a.series_share.series.name)

        elif "series_list" in request.POST:
            series_liste=request.POST["series_list"]
            series=request.POST["series_share"]
            series_liste=series_list.objects.get(id=series_liste)
            series=seriess.objects.get(id=series)
            if len(series_list_content.objects.filter(series=series, series_list_name=series_liste))==0:
                series_list_content.objects.create(series=series, series_list_name=series_liste)
            

        shares = series_shares.objects.filter(hide=0)
        context = {
            "shares":shares,
            "likess":likes_list,
            'save_list':save_list,
            "series_lists":series_lists
        }
            
        return render(request, 'series/series.html',context)    
    shares = series_shares.objects.filter(hide=0)
    context = {
        "shares":shares,
        "likess":likes_list,
    }
        
    return render(request, 'series/series.html',context)




def series_page(request,series_name):
    if request.method == 'POST':
        user=request.user
        val=request.POST.get('val')
        comment=request.POST.get('comment')
        hide=request.POST.get('hide')
        series=seriess.objects.get(name=series_name)
        if hide==True:
            hide=1
        else:
            hide=0
        series_shares.objects.create(user=user, series=series, hide=hide, rate=val, comment=comment)
    
    series=seriess.objects.filter(name=series_name).first()
    series_share=series_shares.objects.filter(series=series, hide=0)
    context = {
        'series':series,
        'shares':series_share
    }
    return render(request, 'series/series_page.html',context)


def series_save(request):
    if request.user.is_authenticated:
        user=request.user
        save_list=[]
        likes_list=[]
        saves=series_saves.objects.filter(user=user)
        likess=series_share_liked.objects.filter(user=user)
        series_lists=series_list.objects.filter(user=user)
        for a in likess:
            likes_list.append(a.series_share.series.name)
            
        for a in saves:
            save_list.append(a.series_share.series.name)
        
        if request.method == "POST":
            if "heart" in request.POST:
                likes_list=[]
                series_share=request.POST["series_share"]
                series_share=series_shares.objects.get(id=series_share)
                like = series_share_liked.objects.filter(user=user,series_share=series_share)
                if len(like) == 0:
                    series_share_liked.objects.create(user=user,series_share=series_share)
                    
                else:
                    like.delete()
                
                likess=series_share_liked.objects.filter(user=user)
                for a in likess:
                    likes_list.append(a.series_share.series.name)
                likes=len(series_share_liked.objects.filter(series_share=series_share))
                series_share.like_count=likes
                series_share.save()
                
            elif "save" in request.POST:
                save_list=[]
                series_save=request.POST["series_save"]
                save=series_saves.objects.filter(user=user, series_share=series_save)
                save.delete()
                    
                saves=series_saves.objects.filter(user=user)
                for a in saves:
                    save_list.append(a.series_share.series.name)

            elif "series_list" in request.POST:
                series_liste=request.POST["series_list"]
                series=request.POST["series_share"]
                series_liste=series_list.objects.get(id=series_liste)
                series=seriess.objects.get(id=series)
                if len(series_list_content.objects.filter(series=series, series_list_name=series_liste))==0:
                    series_list_content.objects.create(series=series, series_list_name=series_liste)
            

        context={
            'shares':saves,
            "likess":likes_list,
            'save_list':save_list,
            "series_lists":series_lists
        }
        return render(request, 'series/series_save.html',context)
    else:
        return redirect('series')