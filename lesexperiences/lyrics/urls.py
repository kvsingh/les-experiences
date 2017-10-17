from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'lyrics'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^analysis$', views.analysis, name='analysis'),
    #url(r'^wordcloud$', views.word_cloud, name='wordcloud'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)