"""podium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

# Django uses urlpatterns for routing. The first argument to url() is a regular
# expression refering to the requested URL. The second argument is either a view
# or a reference to an app within the website. 'name' is a handle that other
# Python code can use to refer to the URL pattern,
urlpatterns = [

    # This refers to a special website where an admin can edit the database.
    url(r'^admin/', admin.site.urls),
    # This refers to another urls.py file whose regexes are matched against the
    # part after 'talks/'.
    url(r'^talks/', include('podium.talks.urls')),
    url(r'^$', views.index, name='index'),

]
