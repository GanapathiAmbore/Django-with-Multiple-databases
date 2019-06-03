from django.db import models
from django.core.validators import RegexValidator

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+91XXXXXXX'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email=models.EmailField()
    image=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)
    address=models.TextField()

    def __str__(self):
        return self.name