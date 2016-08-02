from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, resolve
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from messaging.forms import UserCreateForm
from messaging.models import Category, Message, Reply

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm

    def get_success_url(self):
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return reverse('view_categories')
        return reverse('register')

class CategoryCreateView(CreateView):
    model = Category
    fields = ["category_name"]
    context_object_name = 'form'
    template_name = "messaging/category_form.html"
    success_url = '/start/viewcategories/'

class MessageCreateForm(CreateView):
    model = Message
    fields = ["msg_text"]
    context_object_name = 'form'
    template_name = "messaging/message_form.html"
    # success_url =

class ReplyCreateForm(CreateView):
    model = Reply
    fields = ["reply_text"]
    context_object_name = 'form'
    template_name = 'messaging/reply_form.html'
    # success_url =

class ReplyView(ListView):
    model = Reply
    def get_queryset(self):
        msg_id = self.kwargs.get('msg_id')
        return Reply.objects.all().filter(msg_id=msg_id)

class CategoryView(ListView):
    model = Category

class MessageView(ListView):
    model = Message
    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        return Message.objects.all().filter(category_id=cat_id)

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['category_name']
    success_url = "/start/viewcategories"

class MessageUpdateView(UpdateView):
    model = Message
    fields = ['msg_text']
    def get_success_url(self):
        return reverse('view_categories')

class ReplyUpdateView(UpdateView):
    model = Reply
    fields = ['reply_text']
    def get_success_url(self):
        return reverse('view_reply')

class CategoryDeleteView(DeleteView):
    model = Category
    def get_success_url(self):
        return reverse('view_categories')

class MessageDeleteView(DeleteView):
    model = Message
    def get_success_url(self):
        return reverse('view_message')

class ReplyDeleteView(DeleteView):
    model = Reply
    def get_success_url(self):
        return reverse('view_reply')