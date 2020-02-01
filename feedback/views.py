from django.shortcuts import render
from django.http import HttpResponse
from  .models import Feedback

def get_feedback(request):
    return HttpResponse("hello baby")

