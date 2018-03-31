from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import CashAgreement
from .serializers import CashAgreementSerializer


class CashAgreementViewSet(ModelViewSet):
    queryset = CashAgreement.objects.all()
    serializer_class = CashAgreementSerializer
    permission_classes = (permissions.IsAuthenticated,)



