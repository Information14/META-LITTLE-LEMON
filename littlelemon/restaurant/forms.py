from django.forms import ModelForm
from .models import Booking

class Bookingform(ModelForm): 
    class Meta:
        model = Booking 
        fields = "__all__"

