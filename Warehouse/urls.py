from django.urls import include, path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *

router = routers.DefaultRouter()
router.register(r'mahsulot', MahsulotView)
router.register(r'xomashyo', XomashyoView)
router.register(r'mahsulot_xomashyo', Mahsulot_XomashyoView)
router.register(r'omborxona', OmborxonaView)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,

)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
   path('', include(router.urls)),
]

urlpatterns += [
    path('get_product_info/<str:name>/<int:name_qty>/', get_product_info, name='get_product_info'),
]



