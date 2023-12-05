from django.contrib import admin
from leads.models import Lead,User,Agent,UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)