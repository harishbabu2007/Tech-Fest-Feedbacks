from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.
def index(request):
  return render(request, "api/index.html")


def check(request):
  params = {
    'very_good': 0,
    'good': 0,
    'average': 0,
    'bad': 0,
    'very_bad': 0,
  }
  
  params["very_good"] = VeryGoodModel.objects.count()
  params["good"] = GoodModel.objects.count()
  params["average"] = AverageModel.objects.count()
  params["bad"] = BadModel.objects.count()
  params["very_bad"] = VeryBadModel.objects.count()

  return render(request, "api/check.html", params)

@api_view(["GET"])
def hitGood(request):
  GoodModel.objects.create(yes=True)

  return Response({
    "response": "done"
  })

@api_view(["GET"])
def hitVeryGood(request):
  VeryGoodModel.objects.create(yes=True)

  return Response({
    "response": "done"
  })

@api_view(["GET"])
def hitAverage(request):
  AverageModel.objects.create(yes=True)

  return Response({
    "response": "done"
  })

@api_view(["GET"])
def hitBad(request):
  BadModel.objects.create(yes=True)

  return Response({
    "response": "done"
  })

@api_view(["GET"])
def hitVeryBad(request):
  VeryBadModel.objects.create(yes=True)

  return Response({
    "response": "done"
  })


