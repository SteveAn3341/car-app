from django.shortcuts import render, get_object_or_404, redirect
from car_app.models import Brand
from car_app.models import Car
from car_app.forms import BrandForm , CarForm




def init(request):
    brands = Brand.objects.all()
    data = {'brands': brands}
    return render(request, 'index.html', data)


def details(request,id):
    brands = get_object_or_404(Brand, id=id)
    cars = Car.objects.filter(brand_name = brands)
    data = {'brands':brands,'cars':cars}
    return render(request, "details.html", data)


def models(request,id):
    brands = get_object_or_404(Brand, id=id)
    cars = Car.objects.filter(brand_name = brands)
    data = {'brands':brands,'cars':cars}
    return render(request, "models.html", data)
    

def individual(request,id):
    cars = get_object_or_404(Car, id=id)
    data = {'cars':cars}
    return render(request, 'individual.html', data)




def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = BrandForm()
    return render(request, 'add_brand.html', {'form': form})




def update_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after updating
    else:
        form = BrandForm(instance=brand)
    return render(request, 'update_brand.html', {'form': form})





def delete_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return redirect('index')



def add_car_model(request):
    if request.method =='POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'add_car_model.html', {'form': form})
            
            
def delete_car_model(request, id):
    car_model = get_object_or_404(Car, id=id)
    car_model.delete()
    return redirect('index')
        


def add_car_details(request):
    extra_fields = True
    form = CarForm(request.POST or None, extra=extra_fields)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'add_car_details.html', {'form': form})
           