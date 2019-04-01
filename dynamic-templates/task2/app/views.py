from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app/base.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_home.html',
            'active_page': 'home',
            'items': ''
        }

        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'app/base.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_about.html',
            'active_page': 'about',
            'items': ''
        }

        return render(request, self.template_name, context)




class ContactsView(TemplateView):
    template_name = 'app/base.html'

    def get(self, request, *args, **kwargs):

        context = {
            'path_to_page': 'app/includes/include_contacts.html',
            'active_page': 'contacts',
            'items': ''
        }

        return render(request, self.template_name, context)


class ExamplesView(TemplateView):
    template_name = 'app/base.html'

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
            'active_page': 'examples',
            'items': items
        }
        return render(request, self.template_name,
                      context)
