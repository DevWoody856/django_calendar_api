from django.urls import path, include

from cal.views import HomeView

app_name = 'cal'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('send/', sendGoogle, name='send_google'),
]