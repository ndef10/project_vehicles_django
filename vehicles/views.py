from django.shortcuts import render

# Create your views here.
def v_index(request):
    return render(request, 'vehicles/index.html')