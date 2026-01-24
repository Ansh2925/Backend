from django.http import HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime

def home(request):
    return HttpResponse("<h1>Home</h1>")

def curr_date(request):
    current = datetime.today().ctime()
    return HttpResponse(f"""<h2> {current} </h2>""")




