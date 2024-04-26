from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('responses', ResponseList.as_view(), name='post_delete'),
    path('responses/<int:pk>', ResponseDetail.as_view(), name='post_delete'),
    path('<int:pk>/response_create', ResponseCreate.as_view(), name='post_delete'),
]
