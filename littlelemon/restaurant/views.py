from django.shortcuts import render 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from .serializers import Menuserial, Bookingserial
from .models import Booking, Menu
from .forms import Bookingform
from rest_framework.renderers import HTMLFormRenderer, TemplateHTMLRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import serializers
from datetime import datetime
import json



def home(request): 
    return render(request, "index.html")

def about(request): 
    return render(request, "about.html")


def book(request):
    form = Bookingform()
    if request.method == "POST": 
        form = Bookingform(request.POST)
        if form.is_valid(): 
            form.save()
    context = {'form': form} 
    return render(request, "book.html", context)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def reservations(request): 
    if request.method == "GET":
        try: 
            bookingserial = Booking.objects.all()
            booking = Bookingserial(bookingserial, many=True)
            context = {"booking" : booking.data}
            return Response(context, template_name="bookings.html")
        except Exception as e: 
            return Response({"Inavlid" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    if request.method == "GET": 
        try: 
            menuserial = Menu.objects.all()
            menu = Menuserial(menuserial, many=True)
            context = {'menu': menu.data}
            return Response(context, template_name="menu.html")
        except Exception as e: 
            return Response({"Invalid": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def display_menu_item(request, pk): 
    if request.method == "GET": 
        try: 
            menuserial = Menu.objects.get(pk=pk)
            menu = Menuserial(menuserial)
            context = {'menu': menu.data}
            return Response(context, template_name="menuitem.html")
        except Exception as e: 
            return Response({"Invalid": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def display(request): 
    if request.method == "GET": 
        try: 
            menuserial = Menu.objects.all()
            
            menu_name = request.query_params.get("name")

            if menu_name: 
                menuserial = menuserial.filter(name__icontains=menu_name)


            menu = Menuserial(menuserial, many=True)

            context = {'menu': menu.data}

            return Response(context, template_name="menu.html")
        except Exception as e: 
            return Response({"Invalid": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (Booking.objects.filter(reservation_date=data["reservation_date"]).filter(reservation_slot=data["reservation_slot"]).exists())
        if exist == False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.Serializer("json", bookings)

    return HttpResponse(booking_json, content_type="application/json")
