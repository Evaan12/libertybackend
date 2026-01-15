from django.urls import path
from .views import AboutPageAPIView

urlpatterns = [
path('about/', AboutPageAPIView.as_view(), name='about-page-api'),
]