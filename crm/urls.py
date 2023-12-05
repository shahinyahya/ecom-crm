from django.contrib import admin
from django.urls import path, include
from leads.views import home_page, HomePage, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_page, name='home'),
    path('signup/', SignUpView.as_view(), name='lead-signup'),
    path('login/', LoginView.as_view(), name='lead-login'),
    path('logout/', LogoutView.as_view(), name='lead-logout'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('', HomePage.as_view() , name='home'),             # this is based on class based view
]