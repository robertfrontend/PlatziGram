# PlatziGram URLS
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world', local_views.hello_word),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    # path('admin/', admin.site.urls),

    path('posts/', posts_views.list_posts)
]
