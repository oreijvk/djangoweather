#test commit comment
from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=EA7EB709-F8E8-4065-B92B-A22EF3C5013D")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate>":
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"

        return render(request, 'home.html', {'api': api, 'category_color': category_color})

    else:
        api_requests = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=06460&distance=5&API_KEY=EA7EB709-F8E8-4065-B92B-A22EF3C5013D")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate>":
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"

        return render(request, 'home.html', {'api': api, 'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})