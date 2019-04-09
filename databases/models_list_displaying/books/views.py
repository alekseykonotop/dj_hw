from django.views import generic
from .models import Book
import datetime


class BookListView(generic.ListView):
    template_name = 'templates/books/books_list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f'context in BookListView==> {context}')
        context['paginator'] = False
        return context


class BookListDateView(generic.ListView):
    template_name = 'templates/books/books_list.html'
    model = Book

    def get_queryset(self):
        # create a date object in **kwargs
        year, month, day = map(int, [self.kwargs['year'], self.kwargs['month'], self.kwargs['day']])
        date = datetime.date(year, month, day)

        return Book.objects.filter(pub_date=date)

    def get_context_data(self, **kwargs):
        # create a date object in **kwargs
        year, month, day = map(int, [self.kwargs['year'], self.kwargs['month'], self.kwargs['day']])
        date = datetime.date(year, month, day)

        context = super().get_context_data(**kwargs)
        print(f'context in DateView==> {context}')

        # prev_date
        prev_date_set = Book.objects.filter(pub_date__lt=date).order_by('pub_date')

        #next page
        next_date_set = Book.objects.filter(pub_date__gt=date).order_by('pub_date')

        context['prev_date'] = prev_date_set[len(prev_date_set) - 1] if prev_date_set else ''
        context['next_date'] = next_date_set[0] if next_date_set else ''
        context['paginator'] = True

        return context