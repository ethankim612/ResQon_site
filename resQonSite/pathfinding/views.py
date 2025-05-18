from django.shortcuts import render

# Create your views here.

def pathfinding_view(request):
    return render(request, 'pathfinding/pathfinding.html')
