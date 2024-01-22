from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserDetailSerializer
from apps.users.permissions import UserPermissions

class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissions(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    