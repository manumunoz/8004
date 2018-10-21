from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInst(Page):
    pass


class DecisionsInstWP(WaitPage):
    pass


class DecisionsInst(Page):
    form_model = 'player'
    form_fields = ['symbol','label', 'active', 'count']

    def symbol_error_message(self, value):
        if value != 1:
            return 'In Part 1 your group and appearance are fixed for all 10 rounds'

    def label_error_message(self, value):
        if value != 2:
            return 'In Part 1 your label is randomly assigned in each round'

    def active_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both participants'

    def count_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both participants'


class PointsInstWP(WaitPage):
    pass


class PointsInst(Page):
    form_model = 'player'
    form_fields = ['pay_coord','pay_nocoord']

    def pay_coord_error_message(self, value):
        if value != 1:
            return 'A player in group circle gets 6 points for each coordination with an active relation and pays 2 points for' \
                   'proposing the relation'

    def pay_nocoord_error_message(self, value):
        if value != 3:
            return 'A player get no points if there is no coordination with an active relation but still pays the 2 points' \
                   'for proposing the relation'


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    WelcomeInst,
    DecisionsInstWP,
    DecisionsInst,
    PointsInstWP,
    PointsInst,
    SummaryInstWP,
    SummaryInst,
]
