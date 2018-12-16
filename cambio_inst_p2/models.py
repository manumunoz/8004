from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P2
"""


class Constants(BaseConstants):
    name_in_url = 'cambio_inst_p2'
    players_per_group = None
    num_rounds = 1
    min_pay = 5
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    points_exchange = 1
    currency_exchange = 1000
    exp_currency = "puntos"
    currency = "pesos"
    instructions_template= 'cambio_inst_p2/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3])  # 1: Full, 2: Sticky, 3: Blind
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3

    given_group = models.PositiveIntegerField(
        choices=[
            [1, 'Está fijo y no cambia'],
            [2, 'El computador lo cambia en cada ronda'],
            [3, 'Yo lo puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )

    appearance = models.PositiveIntegerField(
        choices=[
            [1, 'Está fija y no cambia'],
            [2, 'El computador la cambia en cada ronda'],
            [3, 'Yo la puedo cambiar en cada ronda al cambiar mi grupo'],
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

    pay_coord = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord2 = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )

    information = models.PositiveIntegerField(
        choices=[
            [1, 'Ellos pueden ver el grupo que yo elija y mi nueva apariencia'],
            [2, 'Ellos pueden ver el grupo que yo elija y mi apariencia de la Parte 1'],
            [3, 'Ellos no pueden ver el grupo que yo elija sólo mi apariencia de la Parte 1'],
        ],
        widget=widgets.RadioSelect
    )