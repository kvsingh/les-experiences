from django.conf.urls import url

from . import views

app_name = 'lyrics'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^analysis$', views.analysis, name='analysis'),
    url(r'^wordcloud$', views.word_cloud, name='wordcloud'),
]