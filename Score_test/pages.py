from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RandomPayWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.sum_score()
        self.group.ranking_for_groups()
        self.group.given_types()


class RandomPay(Page):
    pass
    # def vars_for_template(self):
    #     return self.player.vars_for_template()


page_sequence = [
    RandomPayWP,
    RandomPay,
]
