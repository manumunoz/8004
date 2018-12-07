from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P2
"""


class Constants(BaseConstants):
    name_in_url = 'cambio_inst_p2'
    players_per_group = None
    num_rounds = 1
    min_pay = 10000
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    exchange = 2
    instructions_template= 'cambio_inst_p2/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    new_symbol = models.PositiveIntegerField(
        choices=[
            [1, 'Están fijos y no cambian'],
            [2, 'El computador los cambia en cada ronda'],
            [3, 'Yo los puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )
