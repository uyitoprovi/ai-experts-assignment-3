"""Views for the books application."""
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):
    """Display a list of all books. Requires user authentication."""
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Display details of a single book. Requires authentication and special permission."""
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    # Permission required to view book details
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(ListView):
    """Display search results for books based on title or author."""
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        """Filter books by search query in title or author fields."""
        query = self.request.GET.get("q")
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        # Return empty queryset if no query provided to avoid None lookup errors
        return Book.objects.none()
