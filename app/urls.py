
from django.urls import path
from app.views import ProfileView,ProfilePost,ProductSearchView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('get/',ProfileView.as_view()),
    path('post/',ProfilePost.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('products/', ProductSearchView.as_view(), name='product-search'),
    
]



