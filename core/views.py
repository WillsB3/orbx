from django.views.generic import TemplateView

hello_world = TemplateView.as_view(template_name='hello-world.html')
