from django.shortcuts import render

from .models import SmartFarm
from .

# Create your views here.
class LedView(generics.ListAPIView):
    get_led = [IsAdminUser]
    queryset = Post.objects.all()
    