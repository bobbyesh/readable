from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from api.models import Article, Language

from core.utils import klassified
from core.services import fetch_article
from core.mixins import ArticleMixin

from .forms import URLForm


def logout_view(request):
    logout(request)
    return redirect('logout_success')


class LogoutSuccessView(TemplateView):
    template_name = 'landing/logout_success.html'


@method_decorator(login_required, name='dispatch')
class HomeView(FormView, LoginRequiredMixin):
    template_name = 'webapp/home.html'
    login_url = 'landing/signin'
    form_class = URLForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        articles = self.request.user.api_article_owner.all()
        context['articles'] = articles
        context['user'] = self.request.user
        return context


    def form_valid(self, form):
        url = form.cleaned_data['url']
        user = self.request.user
        language = Language.objects.get(language='zh')
        article = Article.objects.filter(url=url)
        if article:
            text = article[0].text
        else:
            title, text = fetch_article(url, language='zh')

        Article.objects.get_or_create(title=title, text=text, url=url, language=language, owner=user)
        return super(HomeView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ArticleView(TemplateView, ArticleMixin):
    template_name = 'webapp/sample.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user.username)
        if user is not None:
            context['tokens'], context['counts'] = self.get_article_context(user)
        return context
