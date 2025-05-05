
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderInDateRangeView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('embargo-in-range/', OrderInDateRangeView.as_view(), name='order-in-range'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]
