from django.urls import path

from patentAttorneys.views import PatentAttorneyListView, PatentAttorneyRetrieveView

app_name = 'patentAttorneys'

urlpatterns = [
    path('', PatentAttorneyListView.as_view(), name='patent-attorney-list'),
    path('<int:pk>/', PatentAttorneyRetrieveView.as_view(), name='patent-attorney-retrieve')
    path('/info', )
    path('/led', )
    path('/water', )
    path('/fan', )
    path('/door', )
    
]