from django.urls import path
from service import views
urlpatterns = [
    path('latest-service', views.LatestServiceView.as_view(),),
    path('all-service', views.AllServiceView.as_view(),),
    path('create/', views.CreateServiceView.as_view(),),
    path('detail/<int:pk>', views.DetailServiceView.as_view(),),
    path('update/<int:pk>/', views.UpdateServiceView.as_view(),),
    path('delete/<int:pk>/', views.DeleteServiceView.as_view(),),
]
