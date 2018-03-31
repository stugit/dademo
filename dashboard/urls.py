from .api import CashAgreementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cashagreement', CashAgreementViewSet)

urlpatterns = router.urls
