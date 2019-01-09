from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json

author = 'Manu Munoz'

doc = """
Identity Switch - Allocation between types
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'allocation'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    players = len(names)
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
    # Group Names
    # name_gain = 5
    group_a = 'Lions' #Leones
    group_b = 'Tigers' #Tigres
    group_c = 'Leopards' #Leopardos
    group_d = 'Jaguars' #Jaguares
    group_e = 'Cats' #Gatos
    group_f = 'Coyotes' #Coyotes
    group_g = 'Jackals' #Chacales
    group_h = 'Wolves' #Lobos
    group_i = 'Foxes' #Zorros
    group_j = 'Dogs' #Perros
    #------------------------------------------
    # Dictator
    pie = 10
    #------------------------------------------

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.given_type = int(Constants.attribute[p.id_in_group - 1])

        if self.round_number == 1:
            chosen_player = random.randint(1, Constants.players)
            self.session.vars['chosen_player'] = chosen_player


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    given_type = models.IntegerField() # combination of symbol and preference
    alloc_received = models.IntegerField(initial=0)

    alloc = models.PositiveIntegerField(
        choices=[0,1,2,3,4,5,6,7,8,9,10]
    )

    # 1: 3(1) - 2 (4)
    # 3: 5(1) - 4 (4)
    # 5: 6(1) - 7 (4)
    # 6: 1(1) - 2 (4)
    #
    # 2: 3(1) - 4 (4)
    # 4: 5(1) - 7 (4)
    # 7: 6(1) - 2 (4)



    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
        }

    # def var_between_apps(self):
    #     self.participant.vars['part_fixed_round'] = self.session.vars['paying_round_1']
    #     self.participant.vars['part_fixed_payoff'] = self.player.payoff