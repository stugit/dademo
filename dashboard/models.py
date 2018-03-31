from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class CashAgreement(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    amount = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3)
    issuer = models.CharField(max_length=100)
    time = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return "CashAgreement: {0}, {1}, {2}, {3}".format(self.id, self.amount, self.currency, self.issuer)


class CashIOU(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    amount = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3)
    issuer = models.CharField(max_length=100)
    time = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return "CashIOU: {0}, {1}, {2}, {3}".format(self.id, self.amount, self.currency, self.issuer)


class ChangeIssuerDelegation(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    delegate = models.CharField(max_length=100, null=True, blank=True)
    issuer = models.CharField(max_length=100)
    time = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return "ChangeIssuerDelegation: {0}, {1}, {2}, {3}".format(self.id, self.delegate, self.issuer)


class ProposalToChangeIssuer(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    cashToSwap = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=3)
    targetParty = models.CharField(max_length=100)
    triggerParty = models.CharField(max_length=100)
    time = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return "ProposalToChangeIssuer: {0}, {1}, {2}, {3}".format(self.id, self.cashToSwap, self.currency, self.targetParty)


class SwapProposal(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    cashToSwap = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=3)
    targetParty = models.CharField(max_length=100)
    triggerParty = models.CharField(max_length=100)
    time = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return "SwapProposal: {0}, {1}, {2}, {3}".format(self.id, self.cashToSwap, self.currency, self.targetParty)