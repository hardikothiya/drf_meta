from django.contrib.auth.models import Group
from rest_framework import generics

from ..serializers import GroupSerializer
class ManagerList(generics.ListAPIView):
    permission_classes = []

    queryset = Group.objects.filter(name='managers')
    serializer_class = GroupSerializer
