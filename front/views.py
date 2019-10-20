from django.shortcuts import render

# Create your views here.

class Front:
    def index(request):
        return render(request, 'dashboard/index.html')