from django.shortcuts import render

from .models import *

def home(request):
    data = ""
    return render(request, "index.html", {"data": data})

def area(request):
    data = ""
    return render(request, "area.html", {"data": data})

def shoplist(request, aid):
    data = aid
    filter_key = ""
    if aid == 1:
        filter_key = "EAST"
    elif aid == 2:
        filter_key = "WEST"
    elif aid == 3:
        filter_key = "NORTH"
    elif aid == 4:
        filter_key = "SOUTH"
    elif aid == 5:
        filter_key = "CENTRAL"
    else:
        filter_key = None

    shops = ShopName.objects.filter(area__id=aid)
    print(shops)

    return render(request, "shoplist.html", {"data": data, "filter_key": filter_key, "shops": shops, "aid": aid})

def furnitures(request, sid):
    data = ""
    items = Furniture.objects.filter(shop__id=sid)
    shop = ShopName.objects.get(id=sid)
    return render(request, "furnitures.html", {"data": data, "items": items, "shop": shop})

def detail(request, fid):
    data = ""
    item = Furniture.objects.get(id=fid)
    sid = item.shop.id
    persons = ContactPerson.objects.filter(shop_id=sid)
    return render(request, "detail.html", {"data": data, "item":item, "persons": persons})

def printDoc(request, fid):
    data = ""
    item = Furniture.objects.get(id=fid)
    return render(request, "print.html", {"data": data, "item":item})
