from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pet, Adoption
from django.contrib import messages

# View for listing pets
def pet_list(request):
    available_pets = Pet.objects.filter(is_adopted=False)
    return render(request, 'pets/pet_list.html', {"pets": available_pets})

# View for pet details
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/pet_detail.html', {"pet": pet})

# View for showing adoption form
def adoption_form(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/adoption_form.html', {"pet": pet})

# View to handle adoption submission
@csrf_exempt
def adopt_pet(request, pet_id):
    if request.method == "POST":
        pet = get_object_or_404(Pet, id=pet_id)
        if not pet.is_adopted:
            name = request.POST.get("name")
            if not name:
                messages.error(request, "Please provide your name")
                return redirect('pets:adoption_form', pet_id=pet_id)
            
            try:
                # Create adoption record
                adoption = Adoption.objects.create(
                    pet=pet,
                    adopter_name=name
                )
                
                # Update pet status
                pet.is_adopted = True
                pet.save()
                
                messages.success(request, f"Successfully adopted {pet.name}!")
                return render(request, 'pets/adopt_success.html', {
                    "pet": pet,
                    "owner": name
                })
            except Exception as e:
                messages.error(request, "An error occurred during adoption")
                return redirect('pets:adoption_form', pet_id=pet_id)
        else:
            messages.error(request, "This pet has already been adopted")
            return redirect('pets:adoption_form', pet_id=pet_id)
    
    messages.error(request, "Invalid request method")
    return redirect('pets:adoption_form', pet_id=pet_id)
