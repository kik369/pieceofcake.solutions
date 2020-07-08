from django.views import generic
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'frontpage/index.html'


class HomeView(generic.edit.FormView):
    template_name = 'frontpage/home.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.seng_grid_go()
        return super().form_valid(form)


class ContactSuccessView(generic.TemplateView):
    template_name = 'frontpage/thanks.html'


class ServicesView(generic.TemplateView):
    template_name = 'frontpage/services.html'


class AboutView(generic.TemplateView):
    template_name = 'frontpage/about.html'


def robots(request):
    response = HttpResponse('User-agent: *\nSitemap: http://pieceofcake.solutions/sitemap.xml', content_type='text/plain')
    return response


class SitemapView(generic.TemplateView):
    template_name = 'frontpage/sitemap.xml'