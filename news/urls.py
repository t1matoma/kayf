from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.news_home, name='newsjojo'),
    path('create', views.create, name = 'create'),
    path('<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDelete.as_view(), name='news-delete')
]