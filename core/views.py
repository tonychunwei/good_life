from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Habit
from .serializers import HabitSerializer

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Good Life!")

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
