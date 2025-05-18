from django.shortcuts import render

# Create your views here.

def ai_detection_view(request):
    return render(request, 'ai_detection/ai_detection.html')
