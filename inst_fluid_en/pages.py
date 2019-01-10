from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeP2WP(WaitPage):
    pass


class WelcomeP2(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


class GroupChangeInstWP(WaitPage):
    pass


class GroupChangeInst(Page):
    form_model = 'player'
    form_fields = ['given_group','appearance','label','pay_coord','pay_coord2','information']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def given_group_error_message(self, value):
        if value != 3:
            return 'In Part 2 you can change your group in each round'

    def appearance_error_message(self, value):
        if self.player.treat == 1 or self.player.treat == 4:
            if value != 3:
                return 'In Part 2 you change your appearance when you change your group'
        elif self.player.treat != 1 and self.player.treat != 4:
            if value != 1:
                return 'In Part 2 you cannot change your appearance when you change your group'

    def label_error_message(self, value):
        if value != 2:
            return 'In Part 2 your label is randomly assigned in each round'

    def pay_coord_error_message(self, value):
        if value != 2:
            return 'A player in group triangle gets 4 points for each coordination on Up with an active relation and pays 2 points' \
                   ' for proposing the relation'

    def pay_coord2_error_message(self, value):
        if value != 1:
            return 'A player in group circle gets 6 points for each coordination on Up with an active relation and pays 2 points' \
                   ' for proposing the relation'

    def information_error_message(self, value):
        if self.player.treat == 1:
            if value != 1:
                return 'The other players will see the group you choose as well as your new appearance'
        elif self.player.treat == 2:
            if value != 2:
                return 'The other players will see the group you choose and your appearance from Part 1'
        elif self.player.treat == 3:
            if value != 3:
                return 'The other players will not see the group you choose but only your appearance from Part 1'


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    WelcomeP2WP,
    WelcomeP2,
    GroupChangeInstWP,
    GroupChangeInst,
    SummaryInstWP,
    SummaryInst,
]
