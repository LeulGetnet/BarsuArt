from django.urls import path
from .views import index, detail, original_view

urlpatterns = [
    path('', index, name='index'),
    path('originals/', original_view, name='originals_list'),
    path('detail/<int:id>/', detail, name='detail')
]