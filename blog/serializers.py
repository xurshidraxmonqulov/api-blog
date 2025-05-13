from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Sarlavha kamida 5 ta belgidan iborat bo'lishi kerak.")
        return value

    def validate_content(self, value):
        if "spam" in value.lower():
            raise serializers.ValidationError("Post kontenti 'spam' so‘zini o‘z ichiga olmaydi.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_at']

    def validate_content(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Izoh kamida 10 ta belgidan iborat bo‘lishi kerak.")
        return value
