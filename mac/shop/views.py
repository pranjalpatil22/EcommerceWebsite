from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    
    # params = {'no_of_slides' : nslides,'range' :range(1,nslides), 'product' : products}

    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//3 + ceil((n/3)-(n//3))
        allprods.append([prod, range(1,nslides) , nslides])

    # allprods = [[products, range(1,nslides),nslides],
    #             [products, range(1,nslides),nslides]]
    params = {'allprods' : allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        
        email = request.POST.get('email','')
        phone = request.POST.get('number','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc) 
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank= True
        return render(request, 'shop/contact.html', {'message': 'Contact saved successfully!','thank' : thank})
    return render(request, 'shop/contact.html')



def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category = cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nslides = n//3 + ceil((n/3)-(n//3))
        if len(prod) != 0:
            allprods.append([prod, range(1,nslides) , nslides])

    params = {'allprods' : allprods}
    return render(request,'shop/index.html',params)

def prodView(request,myid):
    # fetch the product using the id 
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request,'shop/prodview.html',{'product': product[0]})

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name','')   
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + request.POST.get('address2','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip','')
        itemsJson = request.POST.get('itemsJson','')
        
        
        print(name,email,address,city,state,zip_code) 

        order = Orders(name=name, email=email,address = address,phone = phone,city = city,state = state,zip_code= zip_code,itemsJson = itemsJson)
        thank = True
        order.save()
        
        
        return render(request, 'shop/checkout.html', {'message': 'Order placed successfully!','thank': thank})
    return render(request, 'shop/checkout.html')


