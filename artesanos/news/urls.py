from django.conf.urls import url
from news import views


#tags of the template
app_name = "news"



urlpatterns= [

    url(r'^noticias/$',views.noticias,name='noticias'),


]
