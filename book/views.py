from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from book.models import books, book_shares, book_saves
import json

# Create your views here.

def index(request):
    
    # with open("book/kitap.json") as fl:
    #     datas=json.load(fl)
            
    # liste = ["id", "name","yazar","type","content","img_url"]
    # for data in datas:
    #     a=1
        
    #     while a<6:
    #         dat= data[str(liste[a])]
    #         dat=dat.replace("\n","")
    #         data[str(liste[a])] = dat
    #         a+=1
            
    #     books.objects.create(name=data[str(liste[1])],author=data[str(liste[2])],type=data[str(liste[3])],content=data[str(liste[4])],img_url=data[str(liste[5])])
    
    # bookss= books.objects.all()
    # for book in bookss:
    #     b=book.img_url
    #     a="book/"+str(b)
    #     book.img_url=a
    #     book.save()

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
    
    # bookss=books.objects.all()
    # print(len(bookss))
    # for book in bookss:
        
    #     a=books.objects.filter(name=book.name,author=book.author)
    #     if len(a)!= 1:
    #         print(len(a))
    #         for b in a:
    #             print(b.name)
                
        # if "Takım" in book.name:
            # book.name=book.name.replace("Ciltli","")
            # book.save()
            # print(book.name)
            
    shares = book_shares.objects.all()
    context = {
        "shares":shares
    }
    
    return render(request, 'book/book.html',context)

def book_page(request,book_name):
    book=books.objects.filter(name=book_name).first()
    context = {
        'book':book,
    }
    return render(request, 'book/book_page.html',context)

# http://127.0.0.1:8000/ --> http://127.0.0.1:8000/book/
def yon(request):
    return redirect('book')


def book_saves(request):
    user=request.user
    saves=book_saves.objects.fiter()