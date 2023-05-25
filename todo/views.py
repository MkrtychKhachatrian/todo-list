from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-create")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-update")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-delete")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TaskUpdateStatusView(View):
    @staticmethod
    def get(request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect("todo:task-list")

    @staticmethod
    def post(request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = request.POST.get("is_done", not task.is_done)
        task.save()
        return redirect("todo:task-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
