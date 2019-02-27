from django.urls import path

from base import views

app_name = 'base'
# base/urls.py
urlpatterns = [
    # ex: /questions/
    path(r'', views.index, name='index'),
    # ex: /questions/3
    path(r'<int:question_id>/', views.detail, name='question_detail')
]
