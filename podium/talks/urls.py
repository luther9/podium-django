from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.session_list_view, name='talks-index'),
    url(r'^submit/$', views.submit_talk_view, name='talks-submit'),
    url(r'^sessions/$', views.session_list_view, name='talks-sessions'),
    # These 2 URLs refer to database record IDs.
    url(r'^sessions/(\d+)/$', views.session_talk_list_view,
        name='talks-sessions-id'),
    url(r'^talks/(\d+)/$', views.talk_detail_view, name='talks-talks-id'),
]
