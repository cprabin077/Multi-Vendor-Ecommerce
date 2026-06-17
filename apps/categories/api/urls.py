from django.urls import path

from apps.categories.api.views import CategoryUpdateAndDelete, CategoryView

urlpatterns = [
    path('', CategoryView.as_view(), name="category"),
    path('<int:pk>', CategoryUpdateAndDelete.as_view(), name="category-update")
]