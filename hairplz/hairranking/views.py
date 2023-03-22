from django.shortcuts import render, redirect
from django.urls import reverse
from .yolov5_handler import run_yolov5_detection


def home(request):
    return render(request, 'index.html')

def take_picture(request):
    return render(request, 'take_picture.html')

def process_ranking(request):
    if request.method == 'POST':
        # Process the image and run YOLOv5 detection
        run_yolov5_detection()

        # Redirect to the 2nd_index page with the result
        return redirect(reverse('2nd_index'))

    return render(request, 'index.html')


def second_index(request):
    return render(request, '2nd_index.html')
