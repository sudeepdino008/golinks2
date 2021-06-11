from django.urls import path, re_path
from . import views

app_name = 'bookmarks'
urlpatterns = [
    path('', views.index, name='index'),
    path('l', views.index, name='index'),
    re_path(r'^add/(?P<alias_inp>[/\w+]*)/$', views.add_alias, name='add_alias'),
    re_path(r'^\w+[/\w+]*$', views.resolve, name='resolve')
]
