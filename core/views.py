from django.http import HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import Login, BookingForm

from .models import Menu



# def home(request):
#     return HttpResponse("<h1>Home</h1>")

def curr_date(request):
    current = datetime.today().ctime()
    return HttpResponse(f"""<h2> {current} </h2>""")

def cars(request, car):
    cars_list = {
        'swift': 'Suzuki Swift',
        'i20': 'Hyundai i20',
        'punch': 'TATA Punch',
        'nexon': 'TATA Nexon',
        'creta': 'Hyundai Creta',
        'seltos': 'Kia Seltos',
    }

    description = cars_list[car]
    return HttpResponse(f'<h2>{car}</h2><br>' + description)

def login(request):
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'core/form.html', context)

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/core/home')
    else:
        form = BookingForm()

    return render(request, 'form.html', {'form': form})

# def about(request):
#     return render(request, 'about.html', {'about': 'This is a dynamic content'})

def menu_by_id(request):
    newMenu = Menu.objects.all()  # newMenu stores all values(which presents in the database) presents in menu model
    newMenu_dict = {'menu' : newMenu}

    return render(request, 'menu.html', newMenu_dict)



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')