from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('web-design/', views.web_design, name='web_design'),
    path('web-hosting/', views.web_hosting, name='web_hosting'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('get-a-quote/', views.get_a_quote, name='get_a_quote'),
]
