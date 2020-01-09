from django.urls import path

from a2.components.pages.views import (
    HomePageView,
    AboutPageView,
    ServicesPageView,
    ContactsPageView,
    PrivacyPageView,
    ProcessPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page_view'),
    path('about/', AboutPageView.as_view(), name='about_page_view'),
    path('services/', ServicesPageView.as_view(), name='services_page_view'),
    path('contacts/', ContactsPageView.as_view(), name='contacts_page_view'),
    path('privacy/', PrivacyPageView.as_view(), name='privacy_page_view'),
    path('process/', ProcessPageView.as_view(), name='process_page_view'),
]
