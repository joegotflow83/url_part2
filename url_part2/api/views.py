ffrom rest_framework import generics

from .models import URL
from .serializers import BookSerializer


class URLListView(generics.ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

