from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions P1
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'switch_inst_p1'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    instructions_template = 'switch_inst_p1/Instructions.html'
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    others = len(names) - 1
    total_circles = 4
    total_triangles = 3
    part_name = 1
    part_fixed = 2
    part_fluid = 3
    part_alloc = 4
    rounds_fixed = 10
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

    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
            'names': len(Constants.names)
        }
