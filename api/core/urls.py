from rest_framework.routers import SimpleRouter

from core.views import CatalogViewSet, CatalogItemViewSet, CatalogView

router = SimpleRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'catalog-date', CatalogView)
router.register(r'catalog-items', CatalogItemViewSet)


urlpatterns = [

]

urlpatterns += router.urls
