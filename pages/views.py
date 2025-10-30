from django.shortcuts import render

def root_page(request):
    return render(request, 'pages/root.html')

def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def projects_page(request):
    return render(request, 'pages/projects.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

