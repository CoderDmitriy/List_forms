from django.urls import path
from .views import HomePageView, GetFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('get_form', GetFormView.as_view(), name='get_form')
]
