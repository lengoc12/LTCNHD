from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Tour
from rest_framework.decorators import action
from .serializers import TourSerializer
# Create your views here.


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.filter(status=True)
    serializer_class = TourSerializer
    #permission_classes = [permissions.IsAuthenticated]  #user dang nhap thi moi duoc truy van
    #list --> Xem danh sachs cac tour du lich
    #..(POST) --> them tour
    #detail --> xem chi tiet cac tour
    #..(PUT) --> cap nhat
    #..(DELETE) --> xoa tour

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    @action(methods=['post'], detail=True, url_path='hide-tour', url_name='hide-tour')
        #/tour/{pk}/hide-tour
    def hide_tour(self, request, pk):
        try:
            t = Tour.objects.get(pk=pk)
            t.status = False
            t.save()
        except Tour.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=TourSerializer(t, context={'request': request}).data, status=status.HTTP_200_OK)


def index(request):
    return render(request, template_name='index.html', context={'name': 'Travel'})

