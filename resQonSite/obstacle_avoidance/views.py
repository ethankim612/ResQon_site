from django.shortcuts import render

# Create your views here.

def obstacle_avoidance_view(request):
    return render(request, 'obstacle_avoidance/obstacle_avoidance.html')
