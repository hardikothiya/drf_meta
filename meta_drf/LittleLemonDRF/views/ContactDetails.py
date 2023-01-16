from django.http import Http404, JsonResponse

from rest_framework.views import APIView
from ..models import ContactDetails
from ..models import Order
from ..serializers import ContactSerializer


class ContactDetails(APIView):
    permission_classes = []

    def get_object(self):
        """
        :param pk:
        :return:
        """
        try:
            return ContactDetails.objects.get(username='customer')
        except Exception:
            raise Http404

    def get(self, request):

        test_data_var = self.get_object()
        print(test_data_var)

        return JsonResponse(test_data_var, safe=False)
