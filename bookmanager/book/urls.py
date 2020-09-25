from django.urls import path
from book.views import index,shop,register,json,method,response
from django.urls import converters
from django.urls.converters import register_converter
from book.views import set_cookie,get_cookie,set_session,get_session
from book.views import login,LoginView

class MobileConverter:
    regex ='1[3-9]\d{9}'

    def to_python(self,value):
        return value

    def to_url(self,value):
        return value
register_converter(MobileConverter,'phone')

urlpatterns=[
    path('index/',index),
    path('<int:city_id>/<phone:Mobile>',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('response/',response),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('login/',login),
    path('LV/',LoginView.as_view())
]