from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about-us/', views.about, name = 'about'),
    path('what-we-render/', views.whatWeRender, name = 'render'),
    path('services/', views.services, name = 'services'),
    path('turnkey-solutions-process-and-approach/', views.turnkey, name = 'turnkey'),
    path('work/', views.work, name = 'work'),
    path('work/<int:pk>/', views.work_image, name = 'work_image'),
    path('clients/', views.client, name = 'client'),
    path('contact/', views.contact, name = 'contact'),
    path('message-sent/', views.enquiry_sent, name = 'success'),
    
]