from django.db.models import QuerySet
from django.utils import timezone


class PartyQuerySet(QuerySet):

    def public(self):
        return self.filter(public=True)

    def upcoming(self):
        return self.filter(when__gt=timezone.now())

    def past(self):
        return self.filter(when__lt=timezone.now())
