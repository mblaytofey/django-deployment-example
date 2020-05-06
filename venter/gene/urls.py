from django.conf.urls import url
from gene import views

#template tagging
app_name = 'gene'

urlpatterns = [

    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
    url('relative/',views.relative,name='relative'),
    url('other/',views.other,name='other'),


]
