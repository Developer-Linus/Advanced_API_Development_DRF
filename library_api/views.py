from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Mixin to allow authenticated users to create a book
class IsAuthenticatedMixin:
    permission_classes = [permissions.IsAuthenticated]

# Custom view for listing and creating authors
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Custom view for retrieving, updating, and deleting author(s)
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Custom view for creating and listing books
class BookListCreateView(IsAuthenticatedMixin, generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Custom view for retrieving, updating, and deleting books
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
