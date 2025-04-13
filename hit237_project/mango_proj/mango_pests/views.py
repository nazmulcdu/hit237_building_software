from django.shortcuts import render
from .pest_data import MangoPestDisease

# Sample data (2 pests for testing)
pests_list = [
    MangoPestDisease(
        id="anthracnose",
        name="Anthracnose",
        brief_desc="Fungal disease causing dark lesions",
        image="anthracnose.jpg"
    ),
    MangoPestDisease(
        id="fruit-fly",
        name="Fruit Fly",
        brief_desc="Insect pest that attacks fruits",
        image="fruit-fly.jpg"
    )
]

def pest_list(request):
    pests_data = [pest.to_dict() for pest in pests_list]
    return render(request, 'mango_pests/list.html', {'pests': pests_data})  # Updated path