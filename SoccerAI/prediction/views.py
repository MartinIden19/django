from django.shortcuts import render
from django.db.models import Q
from .models import Matches

def prediction(request):
    matches = Matches.objects.filter(~Q(Prediction="No")).order_by('-Date','-Time')

    return render(request, 'prediction/prediction.html', {'matches' : matches})

def expresspool(request):
    matches = Matches.objects.filter(~Q(ExpressPrediction="No"))
    return render(request, 'prediction/expresspool.html', {'matches' : matches})
