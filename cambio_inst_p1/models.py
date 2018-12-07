from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P1
"""


class Constants(BaseConstants):
    name_in_url = 'cambio_inst_p1'
    players_per_group = None
    num_rounds = 1
    min_pay = 10000
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    exchange = 2
    total_circles = 4
    total_triangles = 3
    instructions_template = 'cambio_inst_p1/Instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    symbol = models.PositiveIntegerField(
        choices=[
            [1, 'Están fijos y no cambian'],
            [2, 'El computador los cambia en cada ronda'],
            [3, 'Yo los puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )

    label = models.PositiveIntegerField(
        choices=[
            [1, 'Está fija y no cambia'],
            [2, 'El computador la cambia en cada ronda'],
            [3, 'Yo la puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )

    active = models.PositiveIntegerField(
        choices=[
            [1, 'Cuando yo le propongo una relación a otro jugador sin importar si este me propone una relación a mí'],
            [2, 'Cuando otro jugador me propone una relación a mí sin importar si yo le propongo una relación a él'],
            [3, 'Cuando yo le propongo una relación a otro jugador que también me propone una relación a mí']
        ],
        widget=widgets.RadioSelect
    )

    count = models.PositiveIntegerField(
        choices=[
            [1, '5'],
            [2, '4'],
            [3, '3']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )

    pay_nocoord = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )
