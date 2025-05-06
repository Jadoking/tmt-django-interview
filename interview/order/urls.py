
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagsListView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('<int:order_id>/tags/', OrderTagsListView.as_view(), name='order-tags'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]
