from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'CustomUserCreateSerializer'

class UserSerializer(BaseUserSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups', 'user_permissions')
        ref_name = 'CustomUserSerializer'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ReturnAuthorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Author
        fields = ['author_id', 'user_id', 'image', 'biography', 'nickname']

class CreateBookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'

class ReturnBookImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BookImage
        fields = ['image']

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReturnBookSerializer(serializers.ModelSerializer):
    author_id = ReturnAuthorSerializer()
    genders = GenderSerializer(many=True)
    book_cover = serializers.ImageField(use_url=True)
    book_images = ReturnBookImageSerializer(source='bookimage_book_id', many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'book_id', 'title', 'quantity', 'price', 'book_cover', 'description',
            'number_pages', 'format', 'publication_year', 'volume', 'status','author_id', 'genders', 'book_images'
        ]

class CreateBookLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLoan
        fields = '__all__'

class ReturnBookLoanSerializer(serializers.ModelSerializer):
    book_id = ReturnBookSerializer()

    class Meta:
        model = BookLoan
        fields = ['book_id', 'devoluption_date', 'real_devoluption_date', 'status']

class CreateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class ReturnLoanSerializer(serializers.ModelSerializer):
    book_loans = ReturnBookLoanSerializer(source='bookloan_loan_id', many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ['loan_id', 'date', 'total', 'book_loans']