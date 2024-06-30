from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpateView.as_view(), name="post_edit"),
    
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('api/send-comment/<int:pk>', views.PostCreateCommentView.as_view(), name='add_comment'),
    path('api/delete-comment/<int:pk>/', views.PostDeleteCommentView.as_view(), name='delete_comment'),
]
