from django.urls import path
from .views import handle_file_upload

urlpatterns = [
    path('upload-file', handle_file_upload, name='upload-file' )
    
]