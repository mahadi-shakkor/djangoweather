from django.contrib import admin
from django.urls import path,include
from . import views
## hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # This should be present
]

