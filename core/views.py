from django.http import HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime

def home(request):
    return HttpResponse("<h1>Home</h1>")

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


