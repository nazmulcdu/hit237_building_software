from django.shortcuts import render

def test_template(request):
    return render(request, 'mango_pests/test.html')