from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInstWP(WaitPage):
    pass


class WelcomeInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


class DecisionsInstWP(WaitPage):
    pass


class DecisionsInst(Page):
    form_model = 'player'
    form_fields = ['given_group','appearance','label','active','count']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def given_group_error_message(self, value):
        if value != 1:
            return 'In Part 1 your group is fixed for all 10 rounds'

    def appearance_error_message(self, value):
        if value != 1:
            return 'In Part 1 your appearance is fixed for all 10 rounds'

    def label_error_message(self, value):
        if value != 2:
            return 'In Part 1 your label is randomly assigned in each round'

    def active_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both players'

    def count_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both players'


class PointsInstWP(WaitPage):
    pass


class PointsInst(Page):
    form_model = 'player'
    form_fields = ['pay_coord','pay_nocoord']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def pay_coord_error_message(self, value):
        if value != 1:
            return 'A player in group circle gets 6 points for each coordination with an active relation and pays 2 points' \
                   ' for proposing the relation'

    def pay_nocoord_error_message(self, value):
        if value != 3:
            return 'A player get no points if there is no coordination with an active relation but still pays the 2 points' \
                   ' for proposing the relation'


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    WelcomeInstWP,
    WelcomeInst,
    DecisionsInstWP,
    DecisionsInst,
    PointsInstWP,
    PointsInst,
    SummaryInstWP,
    SummaryInst,
]
