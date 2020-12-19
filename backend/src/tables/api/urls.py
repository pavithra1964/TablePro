from django.urls import path

from .views import TableListView, TableDetailView


urlpatterns = [
    path('', TableListView.as_view()),
    path('<pk>', TableDetailView.as_view())
]
