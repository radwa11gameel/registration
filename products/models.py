from django.db import models

class PhoneBrand(models.Model):
    brandName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.brandName


def phone_gallery(request,filename):
    return request.brand.__str__() +'/'+request.name+'.jpg'


class Product(models.Model):
   
    brand = models.ForeignKey(PhoneBrand,on_delete=models.CASCADE,default='DEFAULT VALUE')   
    name = models.CharField(max_length=100)                        
    price = models.DecimalField(max_digits=10, decimal_places=2)                                                                        
    screen = models.DecimalField(max_digits=3,decimal_places=1)      
    image = models.ImageField(blank=True,upload_to=phone_gallery)    
                             


    def __str__(self):
        return self.brand.__str__() + ' ' + self.name

    def fullname(self):
        return self.brand.brandName+' '+self.name
