from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"


    def get(self, request, *args, **kwargs):
        form = CalcForm(request.GET)
        if not form.is_valid():
            if not form.is_bound:
                print(f'start branch not form.is_bound')
                print(f'form.is_bound ==> {form.is_bound}')
                return render(request, self.template_name, {'form': CalcForm()})

            print(f'start branch not form.is_valid()')
            print(f'errors ==> {form.errors}')
            return render(request, self.template_name, {'form': CalcForm(request.GET)})

        print(f'Form is valid')
        initial_fee = form.cleaned_data['initial_fee']
        rate = form.cleaned_data['rate']
        months_count = form.cleaned_data['months_count']
        common_result = round(initial_fee + (initial_fee * int(rate) / 100))
        result = round(common_result / months_count, 2)

        context = {
            'form': form,
            'common_result': common_result,
            'result': result,
        }

        return render(request, self.template_name, context)


