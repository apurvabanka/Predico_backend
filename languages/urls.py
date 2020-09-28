from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',views.LangView)

urlpatterns =[
    path('info/',include(router.urls))

]