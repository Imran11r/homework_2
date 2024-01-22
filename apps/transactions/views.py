from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.transactions.models import Transactions
from apps.transactions.serializers import TransactionsSerializer
from apps.users.models import User
from apps.transactions.permissions import UserPermissions


class TransactionsAPIview(GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = IsAuthenticated

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissions(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

    def post(self, request):
        from_user_id = request.data.get('from_user')
        to_user_id = request.data.get('to_user')
        amount = request.data.get('amount')
        try:
            from_user = User.objects.get(id=from_user_id)
            to_user = User.objects.get(id=to_user_id)
            if float(amount) > float(from_user.balance):
                return Response({'detail': 'Недостаточно средств для перевода'}, status=status.HTTP_400_BAD_REQUEST)
            from_user_balance = float(from_user.balance) - float(amount)
            to_user.balance = float(to_user.balance) + float(amount)
            from_user.save()
            to_user.save()
            transfer = Transactions.objects.create(from_user=from_user, to_user=to_user, amount=amount)
            serializer = TransactionsSerializer(transfer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'detail': 'Неверный формат суммы перевода'}, status=status.HTTP_400_BAD_REQUEST)