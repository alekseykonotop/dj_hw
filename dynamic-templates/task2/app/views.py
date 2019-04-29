from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app/includes/include_home.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_home.html',
            'items': ''
        }

        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'app/includes/include_about.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_about.html',
            'items': ''
        }

        return render(request, self.template_name, context)




class ContactsView(TemplateView):
    template_name = 'app/includes/include_contacts.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_contacts.html',
            'items': ''
        }

        return render(request, self.template_name, context)


class ExamplesView(TemplateView):
    template_name = 'app/includes/include_examples.html'

    def get(self, request, *args, **kwargs):
        items = [{
            'title': 'Apple II',
            'text': 'Легенда',
            'img': 'ii.jpg'
        }, {
            'title': 'Macintosh',
            'text': 'Свежие новинки октября 1983-го',
            'img': 'mac.jpg'
        }, {
            'title': 'iMac',
            'text': 'Оригинальный и прозрачный',
            'img': 'imac.jpg'
        }]
        context = {
            'path_to_page': 'app/includes/include_examples.html',
            'items': items
        }
        return render(request, self.template_name,
                      context)
