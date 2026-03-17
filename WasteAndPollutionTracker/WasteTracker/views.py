from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'WasteTracker/home.html', context)

def maps(request):
    context={}
    return render(request, 'WasteTracker/maps.html', context)

def report(request):
    context={}
    return render(request, 'WasteTracker/report.html', context)

def eventsAndActivities(request):
    context={}
    return render(request, 'WasteTracker/eventsAndActivities.html', context)