from django.shortcuts import get_object_or_404
from rest_framework import views, response, status, viewsets
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalRoomViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(id=self.request.user.id)
        user = get_object_or_404(queryset, id=self.request.user.id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)