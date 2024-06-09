from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime

class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.CharField(max_length=20, null=False, blank=False)

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='author_user_id', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='author_image/')
    biography = models.CharField(max_length=1000, blank=False, null=False)
    nickname = models.CharField(max_length=100, blank=False, null=False)

class Book(models.Model):

    FORMATS = [
        ('ebook', 'ebook'),
        ('physical', 'physical')
    ]

    STATUS = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('refused', 'refused')
    ]

    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    book_cover = models.ImageField(upload_to='cover_book/')
    description = models.CharField(max_length=500, blank=False, null=False)
    number_pages = models.IntegerField()
    format = models.CharField(max_length=20, choices=FORMATS, null=False, blank=False)
    publication_year = models.CharField(max_length=4, null=False, blank=False)
    volume = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, null=False, blank=False, default='pending')
    author_id = models.ForeignKey(Author, related_name='book_author_id', on_delete=models.CASCADE)
    genders = models.ManyToManyField(Gender)

class BookImage(models.Model):
    book_id = models.ForeignKey(Book, related_name='bookimage_book_id', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_image/')

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='loan_user_id', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class BookLoan(models.Model):

    STATUS = [
        ('returned', 'returned'),
        ('delayed', 'delayed'),
        ('borrowed', 'borrowed')
    ]

    book_id = models.ForeignKey(Book, related_name='bookloan_book_id', on_delete=models.CASCADE)
    loan_id = models.ForeignKey(Loan, related_name='bookloan_loan_id', on_delete=models.CASCADE)
    devoluption_date = models.DateField()
    real_devoluption_date = models.DateField()
    status = models.CharField(max_length=30, null=False, blank=False, choices=STATUS)

    def save(self, *args, **kwargs):
        now = datetime.now().date()
        self.devoluption_date = now + timedelta(days=15)
        self.save()