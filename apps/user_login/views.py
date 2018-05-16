from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # response = "HI There"
    # return HttpResponse(response)
    return render(request, 'user_login/index.html')
