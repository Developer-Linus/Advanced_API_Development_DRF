from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    # custom field : number of books written by an author
    book_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'book_count']
    
    def get_book_count(self, obj):
        return obj.books.count()
    
class BookSerializer(serializers.ModelSerializer):
    # Nested serializer for the author
    author = AuthorSerializer(read_only=True)

    # Primary key field for writing author details
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    published_year = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'published_date', 'published_year', 'isbn']
    
    def get_published_year(self, obj):
        return obj.published_date.year
    
    #Custom validation: Ensure ISBN is exactly 13 characters
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError('ISBN must be exaclty 13 characters.')
        return value
    def validate_published_year(self, value):
        if value > date.today():
            raise serializers.ValidationError('Published year cannot be in future.')
        return value
    def validate_published_date(self, value):
        if value>date.today():
            raise serializers.ValidationError('Published date cannot be in future.')
        return value