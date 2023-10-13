from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('evaluate/', views.evaluate, name='evaluate'),
    path('UploadFile/', views.UploadFile, name='UploadFile'),
    path('UploadFile/response.html', views.response, name='response'),
    path('evaluate/about.html', views.about, name='about'),
    path('evaluate/studentlogin.html', views.studentlogin, name='studentlogin'),
    path('evaluate/teacherlogin.html', views.teacherlogin, name='teacherlogin'),
    path('evaluate/upload.html', views.uploadform, name='uploadform'),
    path('ml/', views.ml, name='ml')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)