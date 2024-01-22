from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.transactions.views import TransactionsAPIview

router = DefaultRouter()

router.register('', TransactionsAPIview, 'api_transactions')

urlpatterns = router.urls
