from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from bookapp.models import Book
from bookapp.forms import BookForm
# Create your views here.
class BookViewClass(ListView):
    model=Book

class BookViewClass2(ListView):
    model=Book
    template_name='bookapp/view2.html'

class BookDetailClass(DetailView):
    model=Book

class BookCreateView(CreateView):
    model=Book
    fields=['tital','author','pages','prise']

class BookUpdateClass(UpdateView):
    model=Book
    fields='__all__'
from django.urls import reverse_lazy
class BookDeleteClass(DeleteView):
    model=Book
    success_url=reverse_lazy('booklist')