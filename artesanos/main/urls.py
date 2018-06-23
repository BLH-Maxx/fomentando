from django.conf.urls import url
from main import views


#tags of the template
app_name = "main"



urlpatterns= [

    url(r'^$',views.index,name='index'),
    url(r'^contacto/$',views.contacto,name='contacto'),
    url(r'^donar/$',views.donar,name='donar'),
    url(r'^noticias/$',views.noticias,name='noticias'),
    url(r'^quienes_somos/$',views.quienes_somos,name='quienes_somos'),

]
