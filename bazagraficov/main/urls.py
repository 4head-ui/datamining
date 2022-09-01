from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('faq',views.faq,name='faq'),
    path('grafic/',views.grafic,name='grafic'),
    path('graficline/',views.graficline,name='graficline'),
    path('graficfromadmin/',views.graficadmin,name='graficfromadmin'),
    path('graficfromadminline/',views.graficadminline,name='graficfromadminline'),
    path('graficpltplot/',views.graficpltplot,name='graficpltplot'),
    path('graficpltscatter/',views.graficpltscatter,name='graficpltscatter'),
    path('graficadminplot/',views.graficadminplot,name='graficadminplot'),
    path('graficadminscatter/',views.graficadminscatter,name='graficadminscatter')
]