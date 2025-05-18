from django.shortcuts import render

def starts_view(request):
    return render(request, 'starts/starts.html') 