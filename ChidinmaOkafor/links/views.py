from . import serializers
from .models import Links
from rest_framework import generics, status
from . import models
from rest_framework.response import Response
from rest_framework.decorators import APIView
import datetime
from django.utils import timezone



# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset=Links.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

 
class PostCreateApi(generics.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

 
class PostDetailApi(generics.RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class PostUpdateApi(generics.UpdateAPIView): 
    queryset = Links.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer
 

class PostDeleteApi(generics.DestroyAPIView):
    queryset= Links.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)