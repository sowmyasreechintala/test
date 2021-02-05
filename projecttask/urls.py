"""projecttask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from projecttask import settings
from django.conf.urls.static import static
from task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex),
    path('writer_login_check/',views.writer_login_check,name="writer_login_check"),
    path('insertion_submit/',views.insertion_submit,name="insertion_submit"),
    path('viewer/',views.viewIndex),
    path('viewer_login_check/',views.viewer_login_check,name="viewer_login_check")

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
