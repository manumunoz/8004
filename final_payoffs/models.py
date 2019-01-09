from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'final_payoffs'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    others = len(names) - 1
    attribute = [1,4,1,4,1,1,4]
    attributes = {'1': 1, '2': 4, '3': 1, '4': 4, '5': 1, '6': 1, '7': 4}
    total_circles = 4
    total_triangles = 3
    circle = 1 # Majority
    triangle = 0 # Minority
    part_name = 1
    part_fixed = 2
    part_fluid = 3
    part_alloc = 4
    #------------------------------------------
    # Payoffs
    exp_currency = "points"
    currency = "pesos"
    currency_exchange = 1000
    points_exchange = 1
    min_pay = 10000
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    #------------------------------------------

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # def vars_for_template(self):
    #     final_pay = (self.participant.vars['part_name_payoff'])
    #     return {
    #         'circles_name': self.participant.vars['circles_name'],
    #         'triangles_name': self.participant.vars['triangles_name'],
    #         'circles_label': self.participant.vars['circles_label'],
    #         'triangles_label': self.participant.vars['triangles_label'],
    #         'names': len(Constants.names),
    #         'final_payment': final_pay
    #     }

    def vars_for_template(self):
        final_pay = (self.participant.vars['part_fixed_payoff'] +
                     self.participant.vars['part_fluid_payoff'])
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
            'names': len(Constants.names),
            'part_fixed_round': self.participant.vars['part_fixed_round'],
            'part_fixed_payoff': self.participant.vars['part_fixed_payoff'],
            'part_fluid_round': self.participant.vars['part_fluid_round'],
            'part_fluid_payoff': self.participant.vars['part_fluid_payoff'],
            'final_payment': final_pay
        }