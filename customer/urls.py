from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.customer_list), name='customer_list'),
    path('<int:pk>/', login_required(views.customer_detail), name='customer_detail'),
    path('create', login_required(views.customer_create), name="customer_create"),
    path('<int:pk>/edit', login_required(views.customer_edit), name="customer_edit"),
    path('update/<int:pk>', login_required(views.customer_update), name="customer_update"),
    path('<int:pk>/delete', login_required(views.customer_delete), name="customer_delete")
]
