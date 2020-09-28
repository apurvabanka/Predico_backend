"""shadowfax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from info.views import LoginView,LogoutView,user_info,employeeListView
from dataCluster.views import cluster
from calculator.views import func,LoginView,LogoutView,Register
from prediction.views import Predictions
from serviceability.views import Service
from orders.views import Order

# from travello.views import index

urlpatterns = [
    path('',include('travello.urls')),
    path('clusterdata',cluster.as_view()),
    # path('info',user_info.as_view())
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('api/login',LoginView.as_view()),
    path('api/logout',LogoutView.as_view()),
    # path('api/employee/',employeeListView.as_view())
    path('api/register',Register.as_view()),
    path('calc',func.as_view()),
    path('prediction',Predictions.as_view()),
    path('service',Service.as_view()),
    path('orders',Order.as_view())

    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
