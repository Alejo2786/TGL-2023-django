# urls.py (nombre_app)

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProcesoViewSet, DocumentoProcesoViewSet, ComentarioProcesoViewSet

router = DefaultRouter()
router.register('procesos', ProcesoViewSet)
router.register('documentos', DocumentoProcesoViewSet)
router.register('comentarios', ComentarioProcesoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
