from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.db.models import Q
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status as res_status

class BooksPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'DELETE':
            return request.user.groups.filter(Q(name='Admin') | Q(name='Librarian'))
        
        return request.user.groups.filter(Q(name='Author')).exists()

class AuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'PATCH']:
            return False
        
        return request.user.groups.filter(Q(name='Admin') | Q(name='Librarian'))
    
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            if not request.user.is_authenticated:
                return False
            
            return obj.user_id == request.user

        return False

class AdminLibrarianPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        return request.user.groups.filter(Q(name='Admin') | Q(name='Librarian'))

class GenderView(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = (AdminLibrarianPermission,)

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = (AuthorPermission,)
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'POST', 'DELETE']:
            return CreateAuthorSerializer
        return ReturnAuthorSerializer

class BookImageView(ModelViewSet):
    queryset = BookImage.objects.all()
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ReturnBookImageSerializer

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (BooksPermission,)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'POST', 'DELETE']:
            return CreateBookSerializer
        return ReturnBookSerializer
    
    @api_view(['GET'])
    def approve_book(request, book_id, status):
        found = BookLoan.objects.filter(book_id=book_id).first()
        found.status = status
        found.save()

        return Response(found, status=res_status.HTTP_200_OK)

class BookLoanView(ModelViewSet):
    queryset = BookLoan.objects.all()
    http_method_names = ['get', 'put', 'patch']
    permission_classes = (IsAuthenticated,)
    serializer_class = ReturnBookLoanSerializer
    
    def list(self, request, *args, **kwargs):
        print('entrou na função list')
        found = BookLoan.objects.filter(loan_id__user_id=request.user).exclude(status='returned')
        paginator = self.pagination_class()
        paginated_books = paginator.paginate_queryset(found, request)

        serializer = ReturnBookLoanSerializer(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data) 
    
    @action(detail=False, methods=['GET'])
    def get_all_not_returned(self, request):
        found = BookLoan.objects.exclude(status='returned')
        paginator = self.pagination_class()
        paginated_books = paginator.paginate_queryset(found, request)

        serializer = ReturnBookLoanSerializer(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    @api_view(['GET'])
    def return_book(request, id, date):
        found = BookLoan.objects.filter(id=id).first()
        found.status = 'returned'
        found.real_devoluption_date = date
        found.save()

        book_found = Book.objects.filter(book_id=found.book_id).first()
        book_found.quantity += 1
        book_found.save()

        return Response(found, status=res_status.HTTP_200_OK)

class LoanView(ModelViewSet):
    queryset = Loan.objects.all()
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ReturnLoanSerializer
        
        return CreateLoanSerializer
        
    def create(self, request, *args, **kwargs):
        data = request.data
        data['user_id'] = request.user.id
        serializer = CreateLoanSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=res_status.HTTP_201_CREATED)