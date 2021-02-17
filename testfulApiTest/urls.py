from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('reportList/', views.reportList.as_view()),
    # path('reportList/<int:pk>/', views.reportDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)