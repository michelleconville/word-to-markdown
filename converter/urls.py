from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_document, name='convert_document'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('document/<int:pk>/download/', views.download_markdown, name='download_markdown'),
]