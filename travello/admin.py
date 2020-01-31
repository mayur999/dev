from django.contrib import admin
from .models import Destination
from .models import Photo

# Register your models here.
admin.site.register(Destination)
admin.site.register(Photo)