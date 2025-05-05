from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from interview.order.models import Order
from interview.order.serializers import OrderTagSerializer

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderTagsListView(APIView):
    def get(self, request: Request, order_id: int) -> Response:
        try:
            order = Order.objects.prefetch_related('tags').get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)

        tags = order.tags.all()
        serializer = OrderTagSerializer(tags, many=True)
        return Response(serializer.data, status=200) 
