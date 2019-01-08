from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RandomPayWP(WaitPage):
    pass


class RandomPay(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    RandomPayWP,
    RandomPay,
]
