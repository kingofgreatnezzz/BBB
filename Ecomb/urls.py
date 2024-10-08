from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dispatch.views import signup_view
from rest_framework import permissions

from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="B&B Store",
      default_version='v1',
      description="API documentation for managing product sales",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('dispatch/' ,include('dispatch.urls')),

    path('accounts/', include('django.contrib.auth.urls')), 
    path('signup/', signup_view, name='signup'),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)