from rest_framework import serializers

from .models import CashAgreement
from .models import CashIOU
from .models import ChangeIssuerDelegation
from .models import ProposalToChangeIssuer
from .models import SwapProposal


class CashAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashAgreement
        fields = '__all__'


class CashIOUSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashIOU
        fields = '__all__'


class ChangeIssuerDelegationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChangeIssuerDelegation
        fields = '__all__'


class SwapProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SwapProposal
        fields = '__all__'















