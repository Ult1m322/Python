from django.shortcuts import render
from django.http import HttpResponse
from .models import cars_brand, cars_info

def install(request):
    response_text = []

    brands_data = [
        { "BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9 },
        { "BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8 },
        { "BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9 }
    ]

    for data in brands_data:
        brand, created = cars_brand.objects.get_or_create(
            BRAND_NAME=data["BRAND_NAME"],
            defaults={
                "BRAND_COUNTRY": data["BRAND_COUNTRY"],
                "BRAND_RATING": data["BRAND_RATING"]
            }
        )
        if created:
            response_text.append(f"Brand {data['BRAND_NAME']} created.")
        else:
            response_text.append(f"Brand {data['BRAND_NAME']} already exists.")

    cars_data = [
        { "CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota" },
        { "CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford" },
        { "CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW" }
    ]

    for data in cars_data:
        brand_obj = cars_brand.objects.get(BRAND_NAME=data["CAR_BRAND"])
        car, created = cars_info.objects.get_or_create(
            CAR_NAME=data["CAR_NAME"],
            CAR_MODEL=data["CAR_MODEL"],
            defaults={
                "CAR_PRICE": data["CAR_PRICE"],
                "CAR_BRAND": brand_obj
            }
        )
        if created:
            response_text.append(f"Car {data['CAR_NAME']} created.")
        else:
            response_text.append(f"Car {data['CAR_NAME']} already exists.")

    return HttpResponse("<br>".join(response_text))

def index(request):
    cars = cars_info.objects.select_related('CAR_BRAND').all()
    return render(request, 'duikt_task_kishko/index.html', {'cars': cars})