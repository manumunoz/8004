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
    name_in_url = 'chatting'
    names = ['1','2','3','4']
    # names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 4
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    players = len(names)
    others = len(names) - 1
    attribute = [1,4,1,4,1,1,4]
    attributes = {'1': 1, '2': 4, '3': 1, '4': 4, '5': 1, '6': 1, '7': 4}
    total_circles = 2 #4
    total_triangles = 2 #3
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
    name_gain = 5
    group_a = 'Lions' #Leones
    group_b = 'Tigers' #Tigres
    group_c = 'Leopards' #Leopardos
    group_d = 'Jaguars' #Jaguares
    group_e = 'Cats' #Gatos
    group_f = 'Coyotes' #Coyotes
    group_g = 'Jackals' #Chacales
    group_h = 'Wolves' #Lobos
    group_i = 'Foxed' #Zorros
    group_j = 'Dogs' #Perros
    #------------------------------------------


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.given_type = int(Constants.attribute[p.id_in_group - 1])


class Group(BaseGroup):
    total_group_a = models.IntegerField()
    total_group_b = models.IntegerField()
    total_group_c = models.IntegerField()
    total_group_d = models.IntegerField()
    total_group_e = models.IntegerField()
    total_group_f = models.IntegerField()
    total_group_g = models.IntegerField()
    total_group_h = models.IntegerField()
    total_group_i = models.IntegerField()
    total_group_j = models.IntegerField()
    circles_coord = models.IntegerField(initial=0)
    triangles_coord = models.IntegerField(initial=0)
    circles_name = models.PositiveIntegerField()
    triangles_name = models.PositiveIntegerField()
    circles_label = models.StringField()
    triangles_label = models.StringField()

    def choosing_names(self):
        if self.total_group_a == Constants.total_circles:
            self.circles_coord = 1
            self.circles_name = 1
            self.circles_label = Constants.group_a
        elif self.total_group_b == Constants.total_circles:
            self.circles_coord = 1
            self.circles_name = 2
            self.circles_label = Constants.group_b
        elif self.total_group_c == Constants.total_circles:
            self.circles_coord = 1
            self.circles_name = 3
            self.circles_label = Constants.group_c
        elif self.total_group_d == Constants.total_circles:
            self.circles_coord = 1
            self.circles_name = 4
            self.circles_label = Constants.group_d
        elif self.total_group_e == Constants.total_circles:
            self.circles_coord = 1
            self.circles_name = 5
            self.circles_label = Constants.group_e
        else:
            self.circles_coord = 0

        if self.total_group_f == Constants.total_triangles:
            self.triangles_coord = 1
            self.triangles_name = 6
            self.triangles_label = Constants.group_f
        elif self.total_group_g == Constants.total_triangles:
            self.triangles_coord = 1
            self.triangles_name = 7
            self.triangles_label = Constants.group_g
        elif self.total_group_h == Constants.total_triangles:
            self.triangles_coord = 1
            self.triangles_name = 8
            self.triangles_label = Constants.group_h
        elif self.total_group_i == Constants.total_triangles:
            self.triangles_coord = 1
            self.triangles_name = 9
            self.triangles_label = Constants.group_i
        elif self.total_group_j == Constants.total_triangles:
            self.triangles_coord = 1
            self.triangles_name = 10
            self.triangles_label = Constants.group_j
        else:
            self.triangles_coord = 0

    # def name_gains(self):
    #     for player in self.get_players():
    #         if player.given_type == 1 and self.circles_coord == 1:
    #             player.name_gains = Constants.name_gain
    #         elif player.given_type == 4 and self.triangles_coord == 1:
    #             player.name_gains = Constants.name_gain
    #         else:
    #             player.name_gains = 0

    # def round_payoffs(self):
    #     for player in self.get_players():
    #         player.payoff = player.name_gains


class Player(BasePlayer):
    given_type = models.IntegerField() # combination of symbol and preference
    group_a = models.IntegerField(initial=0)
    group_b = models.IntegerField(initial=0)
    group_c = models.IntegerField(initial=0)
    group_d = models.IntegerField(initial=0)
    group_e = models.IntegerField(initial=0)
    group_f = models.IntegerField(initial=0)
    group_g = models.IntegerField(initial=0)
    group_h = models.IntegerField(initial=0)
    group_i = models.IntegerField(initial=0)
    group_j = models.IntegerField(initial=0)
    name_gains = models.IntegerField()

    group_name = models.PositiveIntegerField(
        choices=[
            [1, "{}%".format(Constants.group_a)],
            [2, "{}%".format(Constants.group_b)],
            [3, "{}%".format(Constants.group_c)],
            [4, "{}%".format(Constants.group_d)],
            [5, "{}%".format(Constants.group_e)],
            [6, "{}%".format(Constants.group_f)],
        ],
    )

    def role(self):
        return {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}[self.id_in_group]

    def chat_nickname(self):
        return 'Player {}'.format(self.role())

    def circle_choice_value(self):
        if self.group_name == 1:
            self.group_a = 1
        elif self.group_name == 2:
            self.group_b = 1
        elif self.group_name == 3:
            self.group_c = 1
        elif self.group_name == 4:
            self.group_d = 1
        elif self.group_name == 5:
            self.group_e = 1

    def triangle_choice_value(self):
        if self.group_name == 6:
            self.group_f = 1
        elif self.group_name == 7:
            self.group_g = 1
        elif self.group_name == 8:
            self.group_h = 1
        elif self.group_name == 9:
            self.group_i = 1
        elif self.group_name == 10:
            self.group_j = 1

    # def set_payoffs(self):
    #     self.participant.vars['part_name_payoff'] = self.name_gains

    def var_between_apps(self):
        self.participant.vars['circles_name'] = self.group.circles_name
        self.participant.vars['triangles_name'] = self.group.triangles_name
        self.participant.vars['circles_label'] = self.group.circles_label
        self.participant.vars['triangles_label'] = self.group.triangles_label
