from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Allocation(Page):
    form_model = 'player'
    form_fields = ['alloc']

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    Allocation,
]
