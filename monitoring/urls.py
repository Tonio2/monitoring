from django.urls import path
from . import views

app_name = "monitoring"
urlpatterns = [
    path('', views.FollowUpListView.as_view(), name='index'),
    path('<int:pk>/', views.FollowUpDetailView.as_view(), name='detail'),
    path('fillout/', views.fillout, name='fillout'),
    path('submit/', views.submit, name='submit')
]
