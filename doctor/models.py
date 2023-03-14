from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Patient(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    blood_pressure = models.CharField(max_length=20)
    allergies = models.TextField(blank=True)
    conditions = models.TextField(blank=True)
    medications = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}"




class MedicalRecord(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    prescription = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.date}"




class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=255)
    medical_license_number = models.CharField(max_length=255)
    patients = models.ManyToManyField(Patient, related_name='doctors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
