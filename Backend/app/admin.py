from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(BookImage)
admin.site.register(Gender)
admin.site.register(Author)
admin.site.register(Loan)
admin.site.register(BookLoan)