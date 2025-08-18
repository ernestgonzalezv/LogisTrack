from django.urls import path

from apps.order_processes.presentation.controllers.orders_controller import OrderController

#from apps.order_processes.presentation.controllers.client_portal_controller import ClientPortalController

urlpatterns = [
   path('orders/distribution', OrderController.as_view(), name='orderDistribution'),
]

