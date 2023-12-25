import random
# from django.db import models
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.core.mail import send_mail
from django.urls import reverse
from leads.models import Agent 
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin          #This mixin is used when the user is authenticated and is an organiser.

class AgentListView(OrganiserAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html' 
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)
    
class AgentCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')
    
    # overiding to add agents from current user (i.e, adding multiple )
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{random.randint(0,1000000000)}")
        form.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )

        send_mail(
            subject="You are invited to be an agent",
            message="You were invited to be an agent on Ecom CRM. Congratulations!!",
            from_email='shahin@ecom.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)        # Also to note: when you create please delete migration physically and the db and create new db if there is any conflict regarding adding default value to any models please add it.

        # agent = form.save(commit=False)
        # agent.organisation = self.request.user.userprofile
        # agent.save()

class AgentDetailView(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)

class AgentUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class= AgentModelForm
    
    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-list')   
class AgentDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse('agents:agent-list')