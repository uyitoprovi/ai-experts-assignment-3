# Bug Explanation

## What was the bug?

The bug was in the `SearchResultsListView` class in `books/views.py`. The `get_queryset()` method was directly passing the search query to Django's `icontains` lookup without checking if the query was `None` or empty:

```python
def get_queryset(self):
    query = self.request.GET.get("q")
    return Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
```

When the search page was accessed without a `q` parameter (e.g., `/books/search/`) or with an empty query (`?q=`), the `query` variable would be `None` or an empty string, causing a `TypeError` because Django's `__icontains` lookup cannot handle `None` values.

## Why did it happen?

The original code did not validate the search query before using it in the database filter. This is a common oversight when handling GET parameters that may be missing or empty.

## Why does your fix actually solve it?

The fix adds a simple check to verify that the query exists before filtering:

```python
def get_queryset(self):
    query = self.request.GET.get("q")
    if query:
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    return Book.objects.none()
```

If no query is provided (or it's empty), the method returns an empty queryset instead of attempting a filter with `None`. This prevents the `TypeError` and provides the expected behavior of showing no results when there's no search term.

## What's one realistic case / edge case your tests still don't cover?

One edge case not covered by the current tests is **SQL injection via the search query**. While Django's ORM provides some protection against SQL injection, the search could be enhanced to:

1. Limit the maximum length of the search query
2. Sanitize special characters that might cause unexpected behavior
3. Handle Unicode characters properly for internationalization

Additionally, the tests don't cover the case where the search query contains only whitespace (e.g., `?q=%20%20%20`), which would currently match books with whitespace in their titles or authors.
