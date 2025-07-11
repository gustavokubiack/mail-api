from .views import SubscriberCreateView
from django.urls import path


urlpatterns = [
    path("subscribers/", SubscriberCreateView.as_view(), name="subscriber-create"),
]
