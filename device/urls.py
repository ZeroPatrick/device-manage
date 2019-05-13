"""定义device的URL模式"""

from django.urls import path, re_path

from . import views
app_name = 'device '

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]
