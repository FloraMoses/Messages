from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from messaging import classview
from messaging.classview import UserCreateView, MessageCreateForm, MessageView, ReplyCreateForm, ReplyView, CategoryView, \
    MessageUpdateView, ReplyUpdateView, CategoryUpdateView, CategoryDeleteView, MessageDeleteView, ReplyDeleteView

urlpatterns = [
    url(r'^register_user/$', UserCreateView.as_view(), name="register"),
    url(r'^$', views.login),

    url(r'^category/create/$', classview.CategoryCreateView.as_view(), name="create_category"),
    url(r'^viewcategories/$', CategoryView.as_view(), name="view_categories"),
    url(r'^category/update/(?P<pk>[0-9]+)/$', CategoryUpdateView.as_view(), name="update_category"),
    url(r'^category/delete/(?P<pk>[0-9]+)/$', CategoryDeleteView.as_view(), name="delete_category"),

    url(r'^message/create/$', MessageCreateForm.as_view(), name="create_message"),
    url(r'^message/view/$', MessageView.as_view(), name="view_message"),
    url(r'^message/update/(?P<pk>[0-9]+)/$', MessageUpdateView.as_view(), name="update_message"),
    url(r'^message/delete/(?P<pk>[0-9]+)/$', MessageDeleteView.as_view(), name="delete_message"),

    url(r'^reply/create/$', ReplyCreateForm.as_view(), name="create_reply"),
    url(r'^reply/view/$', ReplyView.as_view(), name="view_reply"),
    url(r'^reply/update/(?P<pk>[0-9]+)/$', ReplyUpdateView.as_view(), name="update_reply"),
    url(r'^reply/delete/(?P<pk>[0-9]+)/$', ReplyDeleteView.as_view(), name="delete_reply"),
]
