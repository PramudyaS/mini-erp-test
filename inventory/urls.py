from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(views.view_item), name="view_item"),
    path('create', login_required(views.create_item), name="create"),
    path('<int:pk>/edit', login_required(views.edit_item), name="edit_item"),
    path('<int:pk>/manage-stock', login_required(views.manage_stock), name="manage_stock"),
    path('<int:pk>/delete', login_required(views.delete_item), name="delete_item")
]
