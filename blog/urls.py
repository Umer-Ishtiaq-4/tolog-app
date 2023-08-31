
from django.urls import path, include
from . import views
urlpatterns = [

    # Gereral
    path('', views.home, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    # Todo
    path('add-todo/', views.addTodo, name='addTodoPage'),
    path('delete-todo/<int:id>' , views.delete_todo ), 
    path('change-status/<int:id>/<str:status>' , views.change_todo ), 
    # Blogs
    path('blogs/', views.blog, name='blogPage'),
    path('addblog/', views.addNewBlog, name='addBlogPage'),
    path('delete-blog/<int:id>' , views.delete_blog ), 
    path('update-blog/<int:id>/', views.update_blog, name='updateBlogPage'),

]
