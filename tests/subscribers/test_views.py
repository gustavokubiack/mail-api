import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from subscribers.models import Subscriber


@pytest.mark.django_db
def test_create_subscriber_success(mocker):
    mocker.patch("subscribers.services.send_email.send_mail")
    client = APIClient()
    data = {"name": "Bruno", "email": "bruno@example.com"}
    response = client.post(reverse("subscriber-create"), data)
    assert response.status_code == 201
    assert Subscriber.objects.filter(email="bruno@example.com").exists()


@pytest.mark.django_db
def test_create_subscriber_invalid_data():
    client = APIClient()
    data = {"name": "", "email": "not-an-email"}
    response = client.post(reverse("subscriber-create"), data)
    assert response.status_code == 400
    assert "email" in response.data
