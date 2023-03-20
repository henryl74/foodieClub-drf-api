from rest_framework import serializers
from .models import Ingredients


class IngredientsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model
    Adds three extra fields when returning a list of Recipe instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # created_at = serializers.SerializerMethodField()
    # updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Ingredients
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'recipe', 'method'
        ]


class IngredientsDetailSerializer(IngredientsSerializer):
    """
    Serializer for the Ingredients model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
