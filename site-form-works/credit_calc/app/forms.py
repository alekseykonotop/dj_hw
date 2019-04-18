from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.CharField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        print(f'initial_fee ==> {initial_fee}')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        print(f'rate ==> {rate}')
        if not rate or int(rate) < 0 or float(rate) < 0:
            raise forms.ValidationError("Процент не может быть отрицательным")
        print(f'rate 2 ==> {rate}')
        return rate

    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        print(f'months_count ==> {months_count}')
        if not months_count or months_count < 1:
            raise forms.ValidationError("Колличество месяцев должно быть больше 1")
        return months_count

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
