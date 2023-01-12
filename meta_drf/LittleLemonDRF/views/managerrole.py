
from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from rest_framework import generics

from ..serializers import GroupSerializer
class ManagerRole(generics.CreateAPIView):
    permission_classes = []
    serializer_class = GroupSerializer

    def perform_create(self, request):
        id = request.data
        queryset = User.objects.get(name=id['name'])

        user = GroupSerializer(queryset)
        if user.is_valid():
            manager_group = Group.objects.get(name='manager')
            manager_group.user_set.add(user)
            manager_group.save()
            return JsonResponse("hhhh", safe=False)
