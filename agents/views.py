from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from leads.models import Agent 
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html' 
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()
    
class AgentCreateView(LoginRequiredMixin, CreateView):
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
    
