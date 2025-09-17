from . import views
from django.urls import path

urlpatterns = [
    path('',views.view_item, name="view_item"),
    path('create', views.create_item, name="create"),
    path('<int:pk>/edit', views.edit_item, name="edit_item"),
    path('<int:pk>/manage-stock', views.manage_stock, name="manage_stock"),
    path('<int:pk>/delete', views.delete_item, name="delete_item")
]
