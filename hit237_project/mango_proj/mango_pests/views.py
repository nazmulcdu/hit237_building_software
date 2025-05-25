from django.shortcuts import render,redirect,get_object_or_404
from .pest_data import mango_pestdiseases
from .forms import PestReportForm

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

def report_pest(request):
    if request.method == 'POST':
        form = PestReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'mango_pests/confirmation.html')
    else:
        form = PestReportForm()
    return render(request, 'mango_pests/userform.html', {'form': form})

def report_edit(request, pk):
    report = get_object_or_404(PestReportForm, pk=pk)
    if request.method == 'POST':
        form = PestReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # You can define this view later
    else:
        form = PestReportForm(instance=report)
    return render(request, 'mango_pests/userform.html', {'form': form})

def report_delete(request, pk):
    report = get_object_or_404(PestReportForm, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'mango_pests/report_confirm_delete.html', {'report': report})
