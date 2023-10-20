from django.urls import path
from cap.server.views import DoorView, FanView, InfoView, LedView, WarningView, WaterView

app_name = 'server'

urlpatterns = [
    # path('', PatentAttorneyListView.as_view(), name='patent-attorney-list'),
    # path('<int:pk>/', PatentAttorneyRetrieveView.as_view(), name='patent-attorney-retrieve')
    path('/info', InfoView.as_view(), name='info'),
    path('/led', LedView.as_view(), name='led'),
    path('/water', WaterView.as_view(), name='water'),
    path('/fan', FanView.as_view(), name='fan'),
    path('/door', DoorView.as_view(), name='door'),
    path('/warning', WarningView.as_view(), name='warning'),
    
    
]