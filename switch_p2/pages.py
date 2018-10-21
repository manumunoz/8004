from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class BeforeChosenTypeWP(WaitPage):
    def after_all_players_arrive(self):
        # self.group.displaying_network()
        self.group.summing_initial_types()


class ChosenType(Page):
    form_model = 'player'
    form_fields = ['chosen_type']


class BeforeFormationWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.assign_random_names_and_positions()
        self.group.choosing_types()
        self.group.displaying_network()
        self.group.summing_types()


class Formation(Page):
    form_model = 'player'

    def get_form_fields(self):
        other_player_names = list(map(lambda x: x.name, self.player.get_others_in_group()))
        other_player_names.sort()
        return other_player_names

    def before_next_page(self):
        self.player.friends = json.dumps([i.name for i in self.player.get_others_in_group() if getattr(self.player, i.name)])


class BeforeActionWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.forming_network()
        self.group.calculate_props_from_and_links() # una vez generada la red, calculo las props from
        self.group.calculate_degree()
        self.group.linking_costs()


class Action(Page):
    form_model = 'player'
    form_fields = ['action']

    def vars_for_template(self):
        self.group.forming_network()

    # def before_next_page(self):
    #     self.player.calculate_degree()


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_actions()
        self.group.sum_coordinations()
        self.group.coordination_score()
        self.group.values_coordination()
        self.group.round_gains()
        self.group.round_payoffs()
        self.group.forming_network()
        self.group.summing_choices()


class Results(Page):
    def vars_for_template(self):
        self.group.forming_network()


class RandomPay(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_payoff': sum(
                [p.payoff for p in self.player.in_all_rounds()]),
            'paying_round_1': self.session.vars['paying_round_1'],
            'paying_round_2': self.session.vars['paying_round_2'],
        }


page_sequence = [
    BeforeChosenTypeWP,
    ChosenType,
    BeforeFormationWP,
    Formation,
    BeforeActionWP,
    Action,
    BeforeResultsWP,
    Results,
    RandomPay
]
