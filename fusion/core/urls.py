from django.urls import path

from core.views import indexView

urlpatterns = [
    path('', indexView.as_view(), name='index'),
]