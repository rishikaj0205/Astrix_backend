from rest_framework import serializers
from .models import Bestsellings

class bestsellingsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Bestsellings
        fields = "__all__"
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None