from django.shortcuts import render

def prediction(request):
    return render(request, 'prediction/prediction.html')

def expresspool(request):
    return render(request, 'prediction/expresspool.html')
