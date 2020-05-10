''' views.py for our home page and link it up for the entire page '''
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = "thanks.html"


class HomePage(TemplateView):
    template_name = 'index.html'
