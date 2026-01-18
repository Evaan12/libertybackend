from django.urls import path
from .views import AboutPageAPIView, AcademicsPageAPIView # Import new view
from .views import FacilitiesPageAPIView  # Import new Facilities view

urlpatterns = [
    path('about/', AboutPageAPIView.as_view(), name='about-page-api'),
    # Add new path for academics
    path('academics/', AcademicsPageAPIView.as_view(), name='academics-page-api'),
    path('facilities/', FacilitiesPageAPIView.as_view(), name='facilities-page-api'),
]