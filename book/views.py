from tabnanny import check
from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from book.models import books, book_shares, book_saves, book_share_liked, book_list, book_list_content
import json

# Create your views here.

def index(request):
    
    if "term" in request.GET:
        bookss_name=books.objects.filter(name__icontains=request.GET.get('term'))
        bookss_author=books.objects.filter(author__icontains=request.GET.get('term'))
     
        names=list()
        edited_names=list()
        for book in bookss_name:
            names.append(book.name)
        
        for book in bookss_author:
            names.append(book.name)
        
        for name in names:
            if name not in edited_names:
                edited_names.append(name)
                
        return JsonResponse(names, safe=False)
        
    if request.method == "POST":    
        save_list=[]
        likes_list=[]
        user=request.user
        saves=book_saves.objects.filter(user=user)
        likess=book_share_liked.objects.filter(user=user)
        book_lists=book_list.objects.filter(user=user)
        for a in likess:
            likes_list.append(a.book_share.book.name)
            
        for a in saves:
            save_list.append(a.book_share.book.name)
        
        if "heart" in request.POST:
            likes_list=[]
            book_share=request.POST["book_share"]
            book_share=book_shares.objects.get(id=book_share)
            like = book_share_liked.objects.filter(user=user,book_share=book_share)
            if len(like) == 0:
                book_share_liked.objects.create(user=user,book_share=book_share)
                
            else:
                like.delete()
            
            likess=book_share_liked.objects.filter(user=user)
            for a in likess:
                likes_list.append(a.book_share.book.name)
            likes=len(book_share_liked.objects.filter(book_share=book_share))
            book_share.like_count=likes
            book_share.save()
            
        elif "save" in request.POST:
            save_list=[]
            book_save=request.POST["book_save"]
            book_save=book_shares.objects.get(id=book_save)
            save=book_saves.objects.filter(user=user, book_share=book_save)
            if len(save) == 0:
                book_saves.objects.create(user=user, book_share=book_save)
                
            else:
                save.delete()
                
            saves=book_saves.objects.filter(user=user)
            for a in saves:
                save_list.append(a.book_share.book.name)
                
        elif "book_list" in request.POST:
            book_liste=request.POST["book_list"]
            book=request.POST["book_share"]
            book_liste=book_list.objects.get(id=book_liste)
            book=books.objects.get(id=book)
            if len(book_list_content.objects.filter(book=book, book_list_name=book_liste))==0:
                book_list_content.objects.create(book=book, book_list_name=book_liste)
            

        shares = book_shares.objects.filter(hide=0)
        context = {
            "shares":shares,
            "likess":likes_list,
            'save_list':save_list,
            "book_lists":book_lists
        }
        
        return render(request, 'book/book.html',context)
    shares = book_shares.objects.filter(hide=0)
    context = {
        "shares":shares,
    }
    
    return render(request, 'book/book.html',context)


def book_page(request,book_name):    
    if request.method == 'POST':
        user=request.user
        val=request.POST.get('val')
        comment=request.POST.get('comment')
        hide=request.POST.get('hide')
        book=books.objects.get(name=book_name)
        if hide==True:
            hide=1
        else:
            hide=0
        book_shares.objects.create(user=user, book=book, hide=hide, rate=val, comment=comment)

    book=books.objects.filter(name=book_name).first()
    book_share=book_shares.objects.filter(book=book, hide=0)
    context = {
        'book':book,
        'shares':book_share
    }
    return render(request, 'book/book_page.html',context)

# http://127.0.0.1:8000/ --> http://127.0.0.1:8000/book/
def yon(request):
    return redirect('book')

def book_save(request):
    if request.user.is_authenticated:
        user=request.user
        save_list=[]
        likes_list=[]
        saves=book_saves.objects.filter(user=user)
        likess=book_share_liked.objects.filter(user=user)
        book_lists=book_list.objects.filter(user=user)
        for a in likess:
            likes_list.append(a.book_share.book.name)
            
        for a in saves:
            save_list.append(a.book_share.book.name)
            
        if request.method == "POST":
            if "heart" in request.POST:
                likes_list=[]
                book_share=request.POST["book_share"]
                book_share=book_shares.objects.get(id=book_share)
                like = book_share_liked.objects.filter(user=user,book_share=book_share)
                if len(like) == 0:
                    book_share_liked.objects.create(user=user,book_share=book_share)
                    
                else:
                    like.delete()
                
                likess=book_share_liked.objects.filter(user=user)
                for a in likess:
                    likes_list.append(a.book_share.book.name)
                likes=len(book_share_liked.objects.filter(book_share=book_share))
                book_share.like_count=likes
                book_share.save()

            elif "save" in request.POST:
                save_list=[]
                book_save=request.POST["book_save"]
                save=book_saves.objects.filter(user=user, book_share=book_save)
                save.delete()
                    
                saves=book_saves.objects.filter(user=user)
                for a in saves:
                    save_list.append(a.book_share.book.name)
            
            elif "book_list" in request.POST:
                book_liste=request.POST["book_list"]
                book=request.POST["book_share"]
                book_liste=book_list.objects.get(id=book_liste)
                book=books.objects.get(id=book)
                if len(book_list_content.objects.filter(book=book, book_list_name=book_liste))==0:
                    book_list_content.objects.create(book=book, book_list_name=book_liste)
            
        
        context={
            'shares':saves,
            'likess':likes_list,
            'save_list':save_list,
            "book_lists":book_lists
        }
        return render(request, 'book/book_save.html',context)
    else:
        return redirect('book')