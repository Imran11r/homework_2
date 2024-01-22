from rest_framework import serializers
from .models import Transactions

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'

    def create(self, validated_data):
        # Extract 'user' from validated_data
        user = validated_data.pop('user', None)

        # Create the Transactions instance without the 'user' field
        transaction = Transactions.objects.create(**validated_data)

        # If 'user' is provided, set it separately
        if user:
            transaction.user = user
            transaction.save()

        return transaction
