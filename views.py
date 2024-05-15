from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def calculate_fare(request):
    # Your fare calculation logic here
    # For example:
    distance = float(request.GET.get('distance', 0))
    fare = distance * 10  # Assuming fare is 10 KES per kilometer
    return JsonResponse({'fare': fare})
    # Adjust the response format according to your needs
