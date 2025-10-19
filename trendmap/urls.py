from django.urls import path
from django.views.generic import TemplateView

app_name = "trendmap"

urlpatterns = [
    # Serve the template at the app root; name it "index" so the namespaced name is trendmap.index
    path("", TemplateView.as_view(template_name="trendmap/trendmap.html"), name="index"),
]
