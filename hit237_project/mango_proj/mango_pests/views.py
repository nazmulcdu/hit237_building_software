from django.shortcuts import render
from .pest_data import mango_pestdiseases

def home(request):
    return render(request, 'mango_pests/home.html')

def about(request):
    return render(request, 'mango_pests/about.html')

def pest_list(request):
    return render(request, 'mango_pests/list.html', {'pests': mango_pestdiseases})

def pest_detail(request, slug):
    pest = next((p for p in mango_pestdiseases if p.slug == slug), None)
    if not pest:
        return render(request, 'mango_pests/not_found.html', status=404)
    return render(request, 'mango_pests/detail.html', {'pest': pest})

def pest_list_view(request):
    return render(request, 'pests.html', {'pests': mango_pestdiseases})

def preventive_tips(request):
    return render(request, 'mango_pests/preventive_tips.html')
