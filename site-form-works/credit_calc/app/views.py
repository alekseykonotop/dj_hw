from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        if not request.GET:
            return render(request, self.template_name, {'form': CalcForm()})

        form = CalcForm(request.GET)
        context = {
            'form': form
        }
        if not form.is_valid():
            return render(request, self.template_name, context)

        initial_fee = form.cleaned_data['initial_fee']
        rate = form.cleaned_data['rate']
        months_count = form.cleaned_data['months_count']

        context['common_result'] = round(initial_fee + (initial_fee * int(rate) / 100))
        context['result'] = round(context['common_result'] / months_count, 2)

        return render(request, self.template_name, context)






