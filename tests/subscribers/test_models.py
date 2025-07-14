import pytest
from subscribers.models import Subscriber

@pytest.mark.django_db
def test_subscriber_str():
    subscriber = Subscriber(name="João", email="joao@example.com")
    assert str(subscriber) == "João <joao@example.com>"
