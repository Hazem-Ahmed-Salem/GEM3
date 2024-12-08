from rest_framework.serializers import ModelSerializer
from .models import User


class RetrievalUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

    # def update(self, instance,password):
    #     instance.password       = password
    #     instance.save()
    #     return instance

class SignUpSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password',]

    def create(self,validated_data):
        user = User.objects.create(validated_data)
        return user


class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
