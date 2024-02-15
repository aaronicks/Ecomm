from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def category_summary(request):

    categories = Category.objects.all()

    return render(request, 'category_summary.html', {'categories':categories})

def category(request, foo):

    # replace hyphens with spaces
    foo = foo.replace('-', ' ')

    # grabbing the category
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        product = Product.objects.filter(category=category) 
        return render(request, 'category.html', {'products':product, 'category':category})
    except:
        messages.info(request, 'Category Does Not Exist')
        return redirect('index')

    return render(request, 'category.html', {})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',  {'products':products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been Logged In!')
            return redirect('index')
        else:
            messages.success(request, 'Invalid Login Details')
            return redirect('login')
    else:      
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been Logout... Thanks for stoping by')
    return redirect('index')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #login user
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.info(request, 'You have successfully Registered!')
            return redirect('index')
        else:    
            messages.info(request, 'Check your Details and try again')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

