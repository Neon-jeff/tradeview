"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePage,NewHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',HomePage,name='home'),
    path('about/',TemplateView.as_view(template_name='pages/about-us.html'),name='about'),
    path('markets/',TemplateView.as_view(template_name='pages/markets.html'),name='market'),
    path('expert/',TemplateView.as_view(template_name='pages/expert.html'),name='expert'),
    path('accounts/',include('accounts.urls')),
    path('home',NewHome,name='new-home')
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
