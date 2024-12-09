from django.db import models

# Define the choices as a tuple of tuples
FOOD_CHOICES = (
    ("Bruschetta", "Bruschetta"),
    ("Greek salad", "Greek salad"),
    ("Grilled fish", "Grilled fish"),
    ("Lemon dessert", "Lemon dessert"),
    ("Pasta", "Pasta"),
)

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    # Use models.CharField with choices=FOOD_CHOICES
    reservation_food = models.CharField(max_length=50, choices=FOOD_CHOICES)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   image = models.ImageField()

   def __str__(self):
      return self.name