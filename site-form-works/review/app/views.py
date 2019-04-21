from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    template_name = 'app/product_detail.html'
    model = Product

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                text = form.cleaned_data.get('text')
                pk = kwargs['pk']

                product = Product.objects.get(id=pk)
                review = Review.objects.create(text=text, product=product)
                review.save()

                return redirect(reverse('product_detail', kwargs={'pk': kwargs['pk']}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ReviewForm()
        context['form'] = form
        product = Product.objects.get(id=self.kwargs['pk'])
        context['object'] = product
        reviews = Review.objects.filter(product=product)
        context['reviews'] = reviews

        if not self.request.session.get('reviewed_products', False):
            self.request.session["reviewed_products"] = [True]
            context['is_review_exist'] = False

            return context

        if self.kwargs['pk'] in self.request.session["reviewed_products"]:
            context['is_review_exist'] = True
        else:
            self.request.session["reviewed_products"] += [self.kwargs['pk']]
            context['is_review_exist'] = False

        return context




