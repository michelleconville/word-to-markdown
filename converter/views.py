from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'converter/convert_document.html'
    