import pytest
from subscribers.serializers import SubscriberSerializer


@pytest.mark.django_db
def test_valid_subscriber_serializer():
    data = {"name": "Maria", "email": "maria@example.com"}
    serializer = SubscriberSerializer(data=data)
    assert serializer.is_valid()
    subscriber = serializer.save()
    assert subscriber.name == "Maria"
    assert subscriber.email == "maria@example.com"


@pytest.mark.django_db
def test_invalid_subscriber_serializer_duplicate_email(subscriber_factory):
    # subscriber_factory is a pytest fixture you should implement or mock
    subscriber_factory(email="lucas@example.com")
    data = {"name": "Lucas", "email": "lucas@example.com"}
    serializer = SubscriberSerializer(data=data)
    assert not serializer.is_valid()
    assert "email" in serializer.errors
