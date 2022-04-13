from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
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
    shop_obj = []

    for shop in shops:
        personlist = ContactPerson.objects.filter(shop__id=shop.id)
        obj = {
            "shop" : shop,
            "persons": personlist
        }

        shop_obj.append(obj)
    
    print(shop_obj)

    return render(request, "shoplist.html", {"data": data, "filter_key": filter_key, "shops": shop_obj, "aid": aid})

def furnitures(request, sid):
    data = ""
    items = Furniture.objects.filter(shop__id=sid)
    shop = ShopName.objects.get(id=sid)
    return render(request, "furnitures.html", {"data": data, "items": items, "shop": shop})

def orderFunitures(request):
    post_data = request.POST
    print(post_data)
    furnitures = post_data.getlist('furnitures')
    email_addr = post_data['email']
    message_data = post_data['message']
    obj = []
    for data in furnitures:
        id = int(data)
        furniture = Furniture.objects.get(id=id)
        obj.append(furniture)
    
    print("printing furniture OBJECTS")
    print(obj)

    subject, from_email, to = 'Your Selected Furniture From Furniture FM', 'furniturefmcanada@gmail.com', f'{email_addr}'
    text_content = 'This is an important message.'
    html_content = get_template('email.html').render({
        'email': email_addr, 'message': message_data, 'obj': obj
    })
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('/')

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
