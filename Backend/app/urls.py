from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'gender', GenderView)
router.register(r'author', AuthorView)
router.register(r'book_image', BookImageView)
router.register(r'book', BookView)
router.register(r'book_loan', BookLoanView)
router.register(r'loan', LoanView)

urlpatterns = router.urls