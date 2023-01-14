from django.http import HttpResponse
from django.contrib.auth.models import User
def home_page(request):
    print ("Home page")
    return HttpResponse("This is the home page")