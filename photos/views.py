from django.views.generic.base import TemplateView
from photos.models import PhotoUpload


class CarouselView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(CarouselView, self).get_context_data(**kwargs)
        context['photos'] = PhotoUpload.objects.all().order_by('-id')
        return context
