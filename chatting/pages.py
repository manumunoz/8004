from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class WelcomeInst(Page):
    pass

 #    def vars_for_template(self):
 #        final_pay = self.participant.vars['part1_payoff']
 #        return {
 #            'part1_payoff': self.participant.vars['part1_payoff'],
 #            'final_payment': final_pay
 #        }
 #
 # Write this in template: {{part1_payoff|c}} and {{final_payment|c}}

class NameChoice(Page):
    form_model = 'player'
    form_fields = ['group_name']

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)


class NameOutcomeWP(WaitPage):

    def after_all_players_arrive(self):
        self.group.choosing_names()
        self.group.name_gains()


class NameOutcome(Page):

    def before_next_page(self):
        self.player.set_payoffs()


page_sequence = [
    WelcomeInst,
    NameChoice,
    NameOutcomeWP,
    NameOutcome
]
