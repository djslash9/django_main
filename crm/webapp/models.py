from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected field name
    
    def __str__(self):
        return f"{self.full_name} - {self.email} - {self.created_at}"  # Corrected field name