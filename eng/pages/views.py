from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def privacy(request):
    return render(request, 'pages/privacy.html')