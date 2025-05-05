from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class DeactivateOrderView(APIView):
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        order_id = kwargs.get('id')
        if not order_id:
            return Response({"error": "Missing order ID"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = self.queryset.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        if not order.is_active:
            return Response({"message": "Order is already inactive."}, status=status.HTTP_200_OK)

        order.is_active = False
        order.save()

        return Response({"message": f"Order {order.id} has been deactivated."}, status=status.HTTP_200_OK)
