from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    is_adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoptions')
    adopter_name = models.CharField(max_length=200)
    adoption_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pet.name} adopted by {self.adopter_name}"