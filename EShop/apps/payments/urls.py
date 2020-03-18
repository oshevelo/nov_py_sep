from django.urls import path

from . import views  

urlpatterns = [
    path('', views.PaymentList.as_view(), name='PaymentList'),
    path('payment-url/', views.PaymentUrl.as_view(), name='PaymentUrl'),
    path('id/<int:id>/', views.PaymentDetail.as_view(), name='PaymentDetails'),
    path('callback/', views.PaymentSystemCallBack.as_view(), name='PaymentSystemCallBack')
]
