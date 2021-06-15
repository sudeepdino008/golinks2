from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

app_name = 'bookmarks'
urlpatterns = [
    path('', RedirectView.as_view(url='/l')),
    path('l', views.index, name='bookmark_list'),
    re_path(r'^add/(?P<alias_inp>[/\w+-]*)/$', views.add_alias, name='add_alias'),
    re_path(r'^\w+[/\w+-]*$', views.resolve, name='resolve')
]
