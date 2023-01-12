from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..serializers import UserSerializer


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return User.objects.get(id=self.kwargs.get('pk'))

        except User.DoesNotExist:

            raise Http404