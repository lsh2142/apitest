from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import sample_api

urlpatterns = [
    # ...
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'^api-token-refresh/', refresh_jwt_token),
    path(r'api/sample-api', sample_api),
    
    # url(r'^login/', views.obtain_auth_token)
]