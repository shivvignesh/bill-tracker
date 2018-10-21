"""bill_tracke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from billapp import views
urlpatterns = [
	path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('add/',views.add,name='add'),
    path('login/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.signout,name='signout'),
    path('expense/',views.add_expense),
    path('display/',views.display),
    path('monthly/',views.monthly),
    path('delete/<int:pk>',views.delete,name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
