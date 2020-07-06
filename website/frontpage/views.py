from django.views import generic
from django.views.generic.edit import FormView
from .forms import ContactForm


class HomeView(generic.TemplateView):
    template_name = 'frontpage/home.html'


class PieceView(FormView):
    template_name = 'frontpage/piece.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.seng_grid_go()
        return super().form_valid(form)


class ContactSuccessView(generic.TemplateView):
    template_name = 'frontpage/thanks.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add
        context.update({'sheep': 'baa'})
        context['name'] = 67
        return context


class ServicesView(generic.TemplateView):
    template_name = 'frontpage/services.html'


class AboutView(generic.TemplateView):
    template_name = 'frontpage/about.html'


class TestView(generic.TemplateView):
    template_name = 'frontpage/test-content-2.html'
