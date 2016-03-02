from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from blog.views import CreatePost, HomePage, Details, Delete

urlpatterns = [

	url(r'^register$', User_Register.as_view(), name='register'),

	url(r'^create$', CreatePost.as_view(), name = "create"),

	url(r'^details/(?P<slug>[0-9A-Za-z-]+)', Details.as_view(), name = "details"),

	url(r'^delete/(?P<slug>[0-9A-Za-z-]+)', Delete.as_view(), name = "delete")



]