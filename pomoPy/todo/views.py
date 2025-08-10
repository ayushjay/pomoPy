from django.shortcuts import render
from django.contrib.auth import login
from .models import TodoModel
from .forms import RegisterForm, TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "todo/register.html"
    success_url = reverse_lazy('todo:login')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)

class TodoList(ListView):
    model = TodoModel
    template_name = "todo/listtodo.html"
    paginate_by = 3


class TodoDetail(DetailView):
    model = TodoModel
    template_name = "todo/tododetail.html"


class TodoCreate(LoginRequiredMixin, CreateView):
    form_class = TodoForm
    template_name = 'todo/createtodo.html'
    success_url = reverse_lazy('todo:todolist_url')
    # awesome function which sets author to logged in user
    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class TodoUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/updatetodo.html'
    success_url = reverse_lazy("todo:todolist_url")

    # another func which only allows author to edit
    def test_func(self):
        obj = self.get_object()  
        return obj.author == self.request.user

class TodoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TodoModel
    success_url = reverse_lazy("todo:todolist_url")
    template_name = "todo/todo_confirm_delete.html"

    def test_func(self):
        obj = self.get_object()  
        return obj.author == self.request.user

