"""
URL configuration for qrcode_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import HttpResponse
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
goal_dir=current_dir[:-29]+"python_qrcode\\qrcode"
sys.path.append(goal_dir)

from main import QRCode

from main import make  # noqa
from constants import (  # noqa
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H,
)
def run_example(data="http://www.lincolnloop.com", *args, **kwargs):
    qr = QRCode(*args, **kwargs)
    qr.add_data(data)
    im = qr.make_image()
    im.save('../my_qrcode/src/image/output.png')




def index(request):
    text=request.GET.get('text')
    run_example(text)
    return HttpResponse(__file__[:-7]+"output.png")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index)
]
