from django.urls import path
from django.views.generic import RedirectView

from . import views
app_name = 'movieapp'
urlpatterns = [

    path('',views.index,name = 'movie'),
    path('movie/<int:movie_id>/',views.detail,name = 'detail'),
    path('add/',views.add_movie, name = 'add_movie'),
    path('update/<int:id>/', views.alter,name = 'alter'),
    path('delete/<int:id>/',views.delete,name = 'del'),
    path('', RedirectView.as_view(url='/shop/', permanent=True)),
]


