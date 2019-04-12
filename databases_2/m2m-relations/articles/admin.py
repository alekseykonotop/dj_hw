from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Category, Compilation


class CompilationInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0

        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter += 1
        if counter == 0:
            raise ValidationError('Укажите основной раздел')
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class CompilationInline(admin.TabularInline):
    model = Category.articles.through
    extra = 1
    formset = CompilationInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (CompilationInline)


@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    pass