from django.urls import path
from idea_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    #path("", views.home, name="home"),
    path("hello/hello.html/", views.hello, name="hello"),
    path("hello/hello.html/page2.html/", views.page2, name="page2"),
]
# fix the last url when we have time
urlpatterns += staticfiles_urlpatterns()
