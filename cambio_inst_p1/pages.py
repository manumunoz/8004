from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInst(Page):
    pass


class DecisionsInstWP(WaitPage):
    pass


class DecisionsInst(Page):
    form_model = 'player'
    form_fields = ['given_group','appearance','label','active','count']

    def given_group_error_message(self, value):
        if value != 1:
            return 'En la Parte 1 su grupo está fijo por todas las 10 rondas'

    def appearance_error_message(self, value):
        if value != 1:
            return 'En la Parte 1 su apariencia está fijo por todas las 10 rondas'

    def label_error_message(self, value):
        if value != 2:
            return 'En la Parte 1 su etiqueta se asigna aleatoriamente en cada ronda'

    def active_error_message(self, value):
        if value != 3:
            return 'Para que una relación esté activa se requiere que los dos jugadores la propongan'

    def count_error_message(self, value):
        if value != 3:
            return 'Para que una relación esté activa se requiere que los dos jugadores la propongan'


class PointsInstWP(WaitPage):
    pass


class PointsInst(Page):
    form_model = 'player'
    form_fields = ['pay_coord','pay_nocoord']

    def pay_coord_error_message(self, value):
        if value != 1:
            return 'Un jugador en el grupo círculo recibe 6 puntos por cada coordinación con una relación aciva y paga 2 puntos por haber propuesto esa relación'

    def pay_nocoord_error_message(self, value):
        if value != 3:
            return 'Un jugador no recibe puntos si no se coordina con una relación aciva pero aún así paga 2 puntos por haber propuesto esa relación'


class SummaryInstWP(WaitPage):
    pass


class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    WelcomeInst,
    DecisionsInstWP,
    DecisionsInst,
    PointsInstWP,
    PointsInst,
    SummaryInstWP,
    SummaryInst,
]
