<<<<<<< HEAD
from django.confs.url import url
from . import views
urlpatterns = [
        url(r'^$',views.post_list,name='post_list'),
=======
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.post_list,name='post_list'),
>>>>>>> c9abe9142e402cff664fe778467abc4fd2b3dfbf
]
