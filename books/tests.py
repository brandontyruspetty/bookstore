from django.test import TestCase

# to access Book model
from .models import Book

# Create your tests here.


class BookModelTest(TestCase):
    def setUpTestData():
        # set up non-modified objects used by all test methods
        Book.objects.create(name='Pride and Prejudice', author_name='Jane Austen',
                            genre='classic', book_type='hard cover', price='23.71')

    def test_book_name(self):
        # get a book object to test
        book = Book.objects.get(id=1)

        # get the metadata for the 'name' field and use it to query its data
        field_label = book._meta.get_field('name').verbose_name

        # compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        # get a book object to test
        book = Book.objects.get(id=1)

        # get the metadata for the 'author_name' and use it to query its max length
        max_length = book._meta.get_field('author_name').max_length

        # compare the value to the expected result ie. 120
        self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # get_absolute_url() should take you to the detail page of book #1
        # and load the URL /books/list/1
        self.assertEqual(book.get_absolute_url(), '/books/list/1')
