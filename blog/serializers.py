from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [ 'id', 'title', 'description']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'username', 'password'] 


        # Adding Password restriction and also not showing the password in postamn and other places
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True,
        } }

    # Hashing the password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # create token for each user. 
        Token.objects.create(user=user)
        return user
