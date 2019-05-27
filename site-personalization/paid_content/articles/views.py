from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Profile

from .models import Article


# def show_articles(request):
#
#     return render(
#         request,
#         'articles.html'
#     )
#
#
def show_article(request, id):
    article = Article.objects.get(pk=id)
    is_article_paid = article.is_paid_content
    context = {
        'article': article,
    }
    if is_article_paid:
        if 'is_subscribed' not in request.session or not request.session['is_subscribed']:
            context['message'] = 'Только пользователи оформившие подписку могут читать платный контент'

    return render(
        request,
        'article.html',
        context
    )

def index(request):
    return render(request, 'index.html')


class ShowArticlesView(ListView):
    template_name = 'articles.html'
    model = Article

    def get_context_data(self):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }

        return context


def buy_subscription(request):
    context = {}
    request.session.set_expiry(30)
    if 'is_subscribed' in request.session:
        if request.session['is_subscribed']:
            context['message'] = 'Вы уже оформили подписку. Приятного чтения!'
            return render(request, 'buy_subscription.html', context)

    if request.method == 'POST':
        if request.user == None:
            context['message'] = 'Перед оформлением подписки необходимо авторизоваться!'
            return render(request, 'buy_subscription.html', context)

        user = request.user
        user_in_db = Profile.objects.get(id=user.pk)
        if not user_in_db.subscription:
            user_in_db.subscription = True
            user_in_db.save()
            context['message'] = 'Поздравляем, подписка оформлена!'
            request.session['is_subscribed'] = True
            return render(request, 'buy_subscription.html', context)

        else:
            context['message'] = 'Вы уже оформили подписку. Приятного чтения!'
            request.session['is_subscribed'] = True
            return render(request, 'buy_subscription.html', context)

    return render(request, 'buy_subscription.html', context)




