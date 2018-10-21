from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P2
"""


class Constants(BaseConstants):
    name_in_url = 'switch_inst_p2'
    players_per_group = None
    num_rounds = 1
    min_pay = 5
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    exchange = 2
    instructions_template= 'instructions/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    new_symbol = models.PositiveIntegerField(
        choices=[
            [1, 'They are fixed and do not change'],
            [2, 'The computer changes them in each round'],
            [3, 'I can change them in each round'],
        ],
        widget=widgets.RadioSelect
    )
