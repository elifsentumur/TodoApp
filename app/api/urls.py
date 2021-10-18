from django.urls import path
from app.api.views import DeveloperList,DeveloperDetail,ProviderList,ProviderDetail,TaskList

urlpatterns = [
    path('provider/', ProviderList.as_view(), name='provider' ),
    path('provider/<pk>', ProviderDetail.as_view(), name='provider-detail' ),
    path('developer/', DeveloperList.as_view(), name='developer' ),
    path('developer/<slug>', DeveloperDetail.as_view(), name='detail' ),
    path('task/', TaskList.as_view(), name='detail' ),
] 


