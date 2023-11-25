from django.shortcuts import render, redirect
from .forms import LeadForm, LeadUpdateForm
from leads.models import Lead

def home_page(request):
    return render(request, 'index.html')

def leads_page(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)

def lead_create_form(request):
    form = LeadForm()

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads/')

    context = {
        "form": LeadForm()
    }
    return render(request, 'leads/lead_create.html',context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadUpdateForm(instance=lead)

    if request.method == 'POST':
        form = LeadUpdateForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads/')

    context = {
        "form": LeadUpdateForm(),
        "lead": lead
    }

    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads/')

def lead_login(request):
    return render(request, 'login.html')

def lead_register(request):
    return render(request, 'signup.html')