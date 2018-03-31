from django.contrib import admin

from .models import CashAgreement
from .models import CashIOU
from .models import ChangeIssuerDelegation
from .models import ProposalToChangeIssuer
from .models import SwapProposal

admin.site.register(CashAgreement)
admin.site.register(CashIOU)
admin.site.register(ChangeIssuerDelegation)
admin.site.register(ProposalToChangeIssuer)
admin.site.register(SwapProposal)