from rest_framework import serializers
from .models import Booking, Menu


class Bookingserial(serializers.ModelSerializer): 
    class Meta: 
        model = Booking
        fields = "__all__"



class Menuserial(serializers.ModelSerializer): 
    class Meta: 
        model = Menu
        fields = "__all__"
