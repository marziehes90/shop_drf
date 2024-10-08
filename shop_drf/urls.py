from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import BrandViewSet,CategoryViewSet,ProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



route=DefaultRouter()
route.register("brands",BrandViewSet)
route.register("categories",CategoryViewSet)
route.register("products",ProductViewSet,basename='products')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(route.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/doc/',SpectacularSwaggerView .as_view(url_name='schema')),


]
