from rest_framework import generics, permissions, filters
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
# class BookListCreateView(IsAuthenticatedMixin, generics.ListCreateAPIView):
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        # Overridding the existing queryset
        queryset = Book.objects.all()
        #Filter books by genre
        genre = self.request.query_params.get('genre')
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        # filter by author id(e.g api/example/?author_id=1/)
        author_id = self.request.query_params.get('author_id')
        if author_id is not None:
            queryset = queryset.filter(author_id = author_id)
        return queryset
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Enable search and ordering in the database
    search_fields = ['title', 'genre']
    order_fields = ['title', 'published_date', 'genre']

# Custom view for retrieving, updating, and deleting books
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
