from django.urls import path, include
from .views import world, post_view, PostListView


urlpatterns = [
    path('world/', world, name="world"),
    path("all-posts-func/", post_view, name="all_posts_func"),
    path('all-posts-class/', PostListView.as_view(), name='all_posts_class'),
]

