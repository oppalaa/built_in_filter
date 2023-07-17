from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'hai': 'IaM VEry BaD PersOn','dt':dt}
    return render(request,'built_in_filters.html',d)
