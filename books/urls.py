from django.urls import path

from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('addnewbook/', BookCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit',BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
]