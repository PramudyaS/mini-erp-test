from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.view), name="view"),
    path('create', login_required(views.create), name="create"),
    path('<int:pk>/edit', login_required(views.edit), name="edit"),
    path('<int:pk>/update', login_required(views.update), name="update"),
    path('<int:pk>/cancel', login_required(views.cancel), name="cancel")
]
