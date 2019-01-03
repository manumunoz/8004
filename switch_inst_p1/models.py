from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P1
"""


class Constants(BaseConstants):
    name_in_url = 'switch_inst_p1'
    players_per_group = None
    num_rounds = 1
    min_pay = 10000
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    points_exchange = 1
    currency_exchange = 1000
    exp_currency = "points"
    currency = "pesos"
    total_circles = 4
    total_triangles = 3
    instructions_template = 'switch_inst_p1/Instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    given_group = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    appearance = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round by changing my group'],
        ],
        widget=widgets.RadioSelect
    )

    label = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    active = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a connection to another player regardless of he/she proposing a connection to me'],
            [2, 'When another player proposes a connection to me regardless of me proposing a connection to him/her'],
            [3, 'When I propose a connection to a player who also proposes a connection to me']
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
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )

    pay_nocoord = models.PositiveIntegerField(
        choices=[
            [1, 'I gain 6 and pay the cost of 2 = 4 points in total'],
            [2, 'I gain 4 and pay the cost of 2 = 2 points in total'],
            [3, 'I gain 0 and pay the cost of 2 = -2 points in total']
        ],
        widget=widgets.RadioSelect
    )
