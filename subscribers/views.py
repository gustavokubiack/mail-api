from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubscriberSerializer
from .services.send_email import EmailService


class SubscriberCreateView(APIView):
    
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subscriber = serializer.instance
            email_service = EmailService()
            email_service.send_email_to_new_subscriber(subscriber)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
