from rest_framework.serializers import ModelSerializer
from blogapp.models import Post
class PostSerializer(ModelSerializer):
    class Meta():
        model=Post
        fields=['title','body','author']
        depth=1