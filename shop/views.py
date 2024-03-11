from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,Cart,Buy
from .forms import CreateUserForm,LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexs(request):
    template=loader.get_template('indexs.html')
    return HttpResponse(template.render({'request':request}))


def allitem(request):
    template=loader.get_template('showitem.html')
    shop=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(template.render({'shop':shop, 'request':request}))

def showitem(request):
    template=loader.get_template('showitem.html')
    cata='phone'
    shop=ItemDetails.objects.select_related('itemsid').filter(cata=cata)
    return HttpResponse(template.render({'shop':shop, 'request':request}))

def showitemhome(request):
    template=loader.get_template('showitem.html')
    cata='itemhome'
    shop=ItemDetails.objects.select_related('itemsid').filter(cata=cata)
    return HttpResponse(template.render({'shop':shop, 'request':request}))

def showitemelectric(request):
    template=loader.get_template('showitem.html')
    cata='electric'
    shop=ItemDetails.objects.select_related('itemsid').filter(cata=cata)
    return HttpResponse(template.render({'shop':shop, 'request':request}))

def showitemeclaner(request):
    template=loader.get_template('showitem.html')
    cata='claner'
    shop=ItemDetails.objects.select_related('itemsid').filter(cata=cata)
    return HttpResponse(template.render({'shop':shop, 'request':request}))

def s_details(request,id):
    template=loader.get_template('s_details.html')
    currentuser=request.user
    shop=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'shop':shop,
        'request':request
        }
    return HttpResponse(template.render(context))

@csrf_exempt
def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'indexs.html')
    context={'form':form}
    return render(request,'auth_login.html',context)

@csrf_exempt
def auth_logout(request):
     if request.method=="POST":
         logout(request)
         return redirect("/")


@login_required(login_url='/auth_login/')
def s_checkout(request,id):
       template=loader.get_template('s_checkout.html')
       current_user = request.user.id
       cart=Cart.objects.all().filter(Id_user=current_user,Id_product=id).first()
       product=Items.objects.get(id=cart.Id_product)
       context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context))  
def s_add_to_cart(request,id):
    currentuser=request.user
    discount=2
    state=False
    shop=ItemDetails.objects.select_related('itemsid').filter(id=id)
    for item in shop:
         net=item.total-discount
    cart=Cart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
    )
    currentuser=request.user.id
    count=Cart.objects.filter(Id_user=currentuser).count()
    cart.save()
    request.session['countcart']=count
    return redirect("/allitem")
    
@login_required(login_url='/auth_login/')
@csrf_exempt
def Buys(request):
       template=loader.get_template('s_checkout.html')
       name=request.POST.get('name')
       number=request.POST.get('number')
       exp=request.POST.get('exp')
       cvv=request.POST.get('cvv')

       products=Buy(name=name,number=number,exp=exp,cvv=cvv)
       products.save()
       return redirect('/allitem')
