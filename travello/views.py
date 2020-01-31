from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .models import Photo
# Create your views here.
def index(request):
    
    # dests = Destination.objects.all()
    photos = Photo.objects.all()
    return render(request, "index.html", {'photos':photos})