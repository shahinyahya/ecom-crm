from django.shortcuts import render, redirect
from .forms import LeadForm, LeadUpdateForm
from leads.models import Lead
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse

# Class Based Views..
class HomePage(TemplateView):
    template_name = 'index.html'

class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads' 

class LeadDetailView(DetailView):      #instead of specifying object_list in html can give custom object_name.
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead-list')

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadUpdateForm

    def get_success_url(self):
        return reverse('leads:lead-list')
class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')
    
class Login(TemplateView):
    template_name = 'login.html'

class Register(TemplateView):
    template_name = 'signup.html'

# Funcitonal Views

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