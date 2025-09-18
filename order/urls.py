from . import views
from django.urls import path

urlpatterns = [
    path('',views.view, name="view"),
    path('create', views.create, name="create"),
    path('<int:pk>/edit', views.edit, name="edit"),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/cancel', views.cancel, name="cancel")
]
