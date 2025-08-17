from django.urls import path

from apps.users.presentation.controllers.blocks_controller import OrderController

#from apps.users.presentation.controllers.client_portal_controller import ClientPortalController

urlpatterns = [
   path('orders/distribution', OrderController.as_view(), name='orderDistribution'),
]

