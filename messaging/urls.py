from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from messaging import classview
from messaging.classview import UserCreateView, MessageCreateForm, MessageView, ReplyCreateForm, Replyview, CategoryView

urlpatterns = [
    url(r'register_user/$', UserCreateView.as_view(), name="register"),
    url(r'^$', views.login),
    url(r'^category/create/$', login_required(classview.CategoryCreateView.as_view())),
    url(r'^viewcategories/$', CategoryView, name="view_categories"),
    url(r'message/create/$', MessageCreateForm.as_view(), name="create_message"),
    url(r'message/view/$',MessageView.as_view(), name="view_message"),
    url(r'reply/create/$', ReplyCreateForm.as_view(), name="create_reply"),
    url(r'reply/view/$', Replyview.as_view(), name="view_reply"),
]
