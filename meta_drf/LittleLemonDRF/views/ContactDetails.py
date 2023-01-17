from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from rest_framework.response import Response

from rest_framework.views import APIView
from ..models import ContactDetails
from ..models import Order
from ..serializers import ContactSerializer


class ContactDetailsView(APIView):
    permission_classes = []

    permission_classes = []
    authentication_classes = []

    def get_object(self):
        try:

            user = User.objects.get(username=self.request.data['username'])
            return ContactDetails.objects.get(user=user.id)
        except Exception as e:
            raise Http404

    def get(self, request, format=None):
        recod = self.get_object()
        serializer = ContactSerializer(recod)

        # json_data = {
        #     'user': serializer.data['user']['username'],
        #     'number': serializer.data['number'],
        #     'last_name': serializer.data['last_name']
        # }
        # print(json_data)
        # print(serializer.is_valid())
        # if serializer.is_valid():
        #     print(serializer.data)
        # else:
        #     print(serializer.errors)

        return Response (serializer.data)
