from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadForm, LeadUpdateForm, CustomUserCreationForm
from leads.models import Lead
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse

# Class Based Views..
class HomePage(TemplateView):
    template_name = 'index.html'

class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads' 

class LeadDetailView(LoginRequiredMixin, DetailView):      #instead of specifying object_list in html can give custom object_name.
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead-list')
    
    def form_valid(self, form):
        # TODO send email..
        send_mail(
            subject='A lead has been created',
            message='Go to list to see the new lead!',
            from_email='admin@ecomiti.com',
            recipient_list=['benna@ecomiti.com']
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadUpdateForm

    def get_success_url(self):
        return reverse('leads:lead-list')
class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('lead-login')

# class Login(TemplateView):
#     template_name = 'auth/login.html'

# class Register(TemplateView):
#     template_name = 'auth/signup.html'

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

# def lead_login(request):
#     return render(request, 'login.html')

# def lead_register(request):
#     return render(request, 'signup.html')