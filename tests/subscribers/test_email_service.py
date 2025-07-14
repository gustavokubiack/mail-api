import pytest
from subscribers.models import Subscriber
from subscribers.services.send_email import EmailService


@pytest.mark.django_db
def test_send_email_to_new_subscriber(mocker):
    subscriber = Subscriber(name="Ana", email="ana@example.com")
    mock_send_mail = mocker.patch("subscribers.services.send_email.send_mail")

    EmailService().send_email_to_new_subscriber(subscriber)

    mock_send_mail.assert_called_once()
    args, kwargs = mock_send_mail.call_args
    assert subscriber.name in args[1]
    assert subscriber.email in args[3]
