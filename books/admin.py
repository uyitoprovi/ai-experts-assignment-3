from django.contrib import admin
from .models import Book, Reviews


class ReviewsInline(admin.TabularInline):
    model = Reviews


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewsInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
