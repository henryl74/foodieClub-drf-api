from django.db import IntegrityError
from rest_framework import serializers
from favorites.models import Favorite


class favoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the favorites model
    Create method ensures the unique nature of 'owner' relating to 'post'
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = [
            'id', 'created_at', 'owner', 'post',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
