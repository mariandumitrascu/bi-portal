"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings


from biportal import views


urlpatterns = [
    path('',            views.HomePage.as_view(),           name='home'),
    path('bip/',        include('biportal.urls',            namespace='biportal')),
    path('accounts/',   include('accounts.urls',            namespace='accounts')),
    path('accounts/',   include('django.contrib.auth.urls'                      )),
    path('admin/',      admin.site.urls,                    name='admin'),
]

admin.sites.AdminSite.site_header = 'Guardian Report Rendering Portal'
admin.sites.AdminSite.site_title = 'Guardian BI Portal'


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    # reference:
    # simple-image-crop project
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
