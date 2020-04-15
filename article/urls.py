from django.urls import path
from . import views
urlpatterns = [
    path('', views.articleList, name='home'),
    path('category/<int:pk>', views.articleCatList, name='category'),
    path('pr_details/<int:pk>', views.pr_details, name='pr_details'),
    path('new_article', views.newArticle, name='new_article'),
    path('api/articles', views.addArticle, name='add_article'),
    path('api/articles/<int:pk>/delete', views.deleteArticle, name='delete_article'),
    path('api/articles/<int:pk>/edit', views.editFormArticle, name='edit_form_article'),
    path('api/articles/edit/<int:pk>', views.editArticle, name='edit_article'),
    path('pr_details/comment', views.comment, name="comment" ),
    path('pr_details/comments', views.commentEdit, name="comment_edit" )
]

