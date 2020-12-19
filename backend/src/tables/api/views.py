from rest_framework.generics import ListAPIView, RetrieveAPIView

from tables.models import Table
from .serialzers import TableSerializer


class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailView(RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
