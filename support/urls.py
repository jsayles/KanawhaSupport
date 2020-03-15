from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib import admin

from support import views


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),

    path('', views.home, name='home'),

    path('admin/', admin.site.urls),
]
