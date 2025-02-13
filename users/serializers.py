from .models import *
from rest_framework import serializers

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CodeAuthSerializr(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(max_length=6, required=False)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['summit_count', 'pt_count', 'is_approve']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client_position'] = instance.get_client_position_display()
        return representation

