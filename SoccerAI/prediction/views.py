from django.shortcuts import render
from django.db.models import Q
from .models import ClubMatches

def prediction(request):
    matches = ClubMatches.objects.filter(~Q(Prediction="No")).order_by('-Date','-Time')
    return render(request, 'prediction/prediction.html', {'matches' : matches})

def expresspool(request):
    matches = ClubMatches.objects.filter(~Q(ExpressPrediction="No")).order_by('-Date','-Time')
    return render(request, 'prediction/expresspool.html', {'matches' : matches})
