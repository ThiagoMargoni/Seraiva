from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# def return_user_group(request):
#     if request.user.is_authenticated:
#         groups = request.user.groups.all()

#         group_names = [group.name for group in groups]

#         return JsonResponse({'grupos': nomes_dos_grupos})
#     else:
#         return JsonResponse({'Error': 'Authentication Required'}, status=401)

class GenderView(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    
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

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'POST', 'DELETE']:
            return CreateBookSerializer
        return ReturnBookSerializer

class BookLoanView(ModelViewSet):
    queryset = BookLoan.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return CreateBookLoanSerializer
        return ReturnBookLoanSerializer

class LoanView(ModelViewSet):
    queryset = Loan.objects.all()
    http_method_names = ['get']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ReturnLoanSerializer