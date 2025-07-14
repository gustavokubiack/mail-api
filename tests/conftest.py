import pytest
from subscribers.models import Subscriber


@pytest.fixture
def subscriber_factory():
    def create_subscriber(**kwargs):
        return Subscriber.objects.create(
            name=kwargs.get("name", "Default Name"),
            email=kwargs.get("email", "default@example.com")
        )
    return create_subscriber
