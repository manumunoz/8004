from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'chatting'
    periods = 1
    num_rounds = periods
    circle = 1 # Majority
    triangle = 0 # Minority
    names = ['1','2','3','4','5','6','7']
    attribute = [1,4,1,4,1,1,4]
    attributes = {'1': 1, '2': 4, '3': 1, '4': 4, '5': 1, '6': 1, '7': 4}
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    points_exchange = 1
    currency_exchange = 1000
    exp_currency = "points"
    currency = "pesos"
    personal = 1
    others = len(names) - 1
    exchange = 2
    players_per_group = len(names)

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.given_type = int(Constants.attribute[p.id_in_group - 1])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    given_type = models.IntegerField() # combination of symbol and preference

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        elif self.id_in_group == 2:
            return 'A'
        elif self.id_in_group == 3:
            return 'B'
        elif self.id_in_group == 4:
            return 'B'
        elif self.id_in_group == 5:
            return 'C'
        elif self.id_in_group == 6:
            return 'D'
        elif self.id_in_group == 7:
            return 'C'

    def chat_nickname(self):
        return 'Player {}'.format(self.role())