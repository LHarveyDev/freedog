from django.shortcuts import render

# Create your views here.


def facilities(request):

    return render(request, 'facilities/facilities.html')
