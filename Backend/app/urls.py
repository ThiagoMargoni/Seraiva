from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

router.register(r'gender', GenderView)
router.register(r'author', AuthorView)
router.register(r'book_image', BookImageView)
router.register(r'book', BookView)
router.register(r'book_loan', BookLoanView)
router.register(r'loan', LoanView)

urlpatterns = router.urls

urlpatterns.append(path('book_loan/return_book/<int:id>/<str:date>/', BookLoanView.return_book, name='return_book'))
urlpatterns.append(path('book/approve_book/<int:book_id>/<str:status>/', BookLoanView.return_book, name='approve_book'))