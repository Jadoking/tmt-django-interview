from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class TagOrdersListView(APIView):
    def get(self, request: Request, tag_id: int) -> Response:
        try:
            tag = OrderTag.objects.prefetch_related('orders__inventory').get(id=tag_id)
        except OrderTag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=404)

        orders = tag.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)
