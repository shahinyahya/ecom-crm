from django.contrib import admin
from leads.models import Lead,User,Agent,UserProfle

admin.site.register(User)
admin.site.register(UserProfle)
admin.site.register(Lead)
admin.site.register(Agent)