from django.http import (
    HttpResponseNotFound,
    HttpResponseServerError
)

from django.contrib import messages
from django.template.loader import get_template
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from a2.components.pages.forms import ContactsForm


def page_not_found(request):
    template = get_template('pages/404.html')
    html = template.render()
    return HttpResponseNotFound(html)


def server_error(request):
    template = get_template('pages/500.html')
    html = template.render()
    return HttpResponseServerError(html)


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServicesPageView(TemplateView):
    template_name = "pages/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactsPageView(FormView):
    template_name = "pages/contacts.html"
    form_class = ContactsForm
    success_url = '/contacts/#form'

    def form_invalid(self, form):
        messages.error(self.request, 'Form submit error!', extra_tags='danger')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Your message successfully submitted! We will contact you within 24h!', extra_tags='success')
        form.send_email(form)
        return super().form_valid(form)


class PrivacyPageView(TemplateView):
    template_name = "pages/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProcessPageView(TemplateView):
    template_name = "pages/process.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
