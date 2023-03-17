from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    medical_history = models.TextField()
    
    def __str__(self):
        return self.email


class SensorData(models.Model):
    sensor_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vital_sign = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.sensor_id) + " - " + self.vital_sign


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email


class MachineLearningModel(models.Model):
    model_name = models.CharField(max_length=50)
    description = models.TextField()
    accuracy = models.DecimalField(max_digits=10, decimal_places=2)
    date_trained = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.model_name
