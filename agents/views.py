from typing import Any
from django.db import models
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse
from leads.models import Agent 
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin          #This mixin is used when the user is authenticated and is an organiser.

class AgentListView(OrganiserAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html' 
    context_object_name = 'agents'

    def get_queryset(self):
        organistaion = self.request.user.userprofile
        return Agent.objects.filter(organistaion = organistaion)
    
class AgentCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')
    
    # overiding to add agents from current user (i.e, adding multiple )
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user
        agent.save()
        return super(AgentCreateView, self).form_valid(form)        # Also to note: when you create please delete migration physically and the db and create new db if there is any conflict regarding adding default value to any models please add it.

class AgentDetailView(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organistaion = self.request.user.userprofile
        return Agent.objects.filter(organistaion = organistaion)

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
        organistaion = self.request.user.userprofile
        return Agent.objects.filter(organistaion = organistaion)

    def get_success_url(self):
        return reverse('agents:agent-list')