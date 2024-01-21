from random import randint
from time import sleep
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from .models import Author, Book
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "age")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("author", "title", "description")


def author_list_create_view(request):
    author_form = AuthorForm()

    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            author_form = AuthorForm()

    response = render(
        request,
        "author_list_create.html",
        {
            "base_template": "base_htmx.html" if request.htmx else "base.html",
            "authors": Author.objects.all(),
            "author_form": author_form
        },
    )

    return response


def author_delete_view(request, id):
    sleep(2)

    if randint(0, 1):
        # Was not deleted
        return redirect("store-author-list-create")

    Author.objects.get(id=id).delete()
    return redirect("store-author-list-create")


class AuthorListView(ListView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("author-list")
