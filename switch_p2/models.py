from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import OrderedDict
import json
import itertools

author = 'Manu Munoz'

doc = """
Identity Switch - Networks: P2
"""


class Constants(BaseConstants):
    name_in_url = 'id_switch_p2'
    num_rounds = 10
    circle = 1 # Majority
    triangle = 0 # Minority
    names = ['1','2','3','4','5','6','7']
    attribute = [1,4,1,4,1,1,4]
    attributes = {'1': 1, '2': 4, '3': 1, '4': 4, '5': 1, '6': 1, '7': 4}
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    personal = 1
    others = len(names) - 1
    exchange = 2
    players_per_group = len(names)
    instructions_template = 'switch_p2/Instructions.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3]) #1: Full, 2:Sticky, 3:Blind
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)
        num_players_err = 'Too many participants for such a short name list'
        # the following may create issues with mTurk sessions where num participants is doubled
        assert len(Constants.names) <= self.session.num_participants, num_players_err
        '''
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            # random.shuffle(cur_names)
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]
        '''
        for p in self.get_players():
            p.given_type = int(Constants.attribute[p.id_in_group - 1])
            if p.given_type == 1: # circle-circle
                p.was_circle = 1
            else: # triangle-triangle
                p.was_circle = 0

        if self.round_number == 1:
            paying_round_2 = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round_2'] = paying_round_2


class Group(BaseGroup):
    total_init_circles = models.IntegerField()
    total_init_triangles = models.IntegerField()
    total_circles = models.IntegerField()
    total_triangles = models.IntegerField()
    total_up = models.IntegerField()
    total_down = models.IntegerField()
    network_data = models.LongStringField()

    def assign_random_names_and_positions(self):
        name_indexes = random.sample(range(7), 7)
        positions = random.sample(range(7), 7)
        i = 0
        for p in self.get_players():
            p.name = Constants.names[name_indexes[i]]
            p.position = positions[i] + 1
            i += 1

    def generate_nodes(self):
        players = self.get_players()
        players.sort(key=lambda x: x.position)
        return [{'data': {'id': p.name, 'name': p.name, 'action': p.action, 'given': p.given_type,
                           'shape': p.chosen_type, 'location': p.position, 'treat': p.treat}, 'group': 'nodes'}
                for p in players]

    def displaying_network(self):
        nodes = self.generate_nodes()
        edges = []
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def forming_network(self):
        nodes = self.generate_nodes()
        edges = []
        for p in self.get_players():
            friends = json.loads(p.friends)
            edges.extend(
                [{'data': {'id': p.name + '_' + str(i), 'source': p.name, 'target': i}, 'group': 'edges'}
                 for i in friends])

            # Copio el valor de las propuestas recogido en las variables con numbre (1,2,3,...) a
            # proo_to_1, prop_to_2, ...
            for i in friends:
                setattr(p, 'prop_to_' + i, getattr(p, i))

        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    # def choosing_types(self):
    #     for player in self.get_players():
    #         if player.given_type == 1:
    #             player.chosen_type = 1
    #             player.is_circle = 1
    #             player.liked_action = 1
    #         else:
    #             player.chosen_type = 4
    #             player.is_circle = 0
    #             player.liked_action = 0

    def choosing_types(self):
        for player in self.get_players():
            if player.chosen_type == 1:
                player.is_circle = 1
                player.liked_action = 1
            elif player.chosen_type == 2:
                player.is_circle = 0
                player.liked_action = 0
            elif player.chosen_type == 3:
                player.is_circle = 1
                player.liked_action = 1
            else:
                player.is_circle = 0
                player.liked_action = 0

    def summing_initial_types(self):
        players = self.get_players()
        init_circles = [p.was_circle for p in players]
        self.total_init_circles = sum(init_circles)
        self.total_init_triangles = len(Constants.names)-self.total_init_circles

    def summing_types(self):
        players = self.get_players()
        circles = [p.is_circle for p in players]
        self.total_circles = sum(circles)
        self.total_triangles = len(Constants.names)-self.total_circles


    def calculate_props_from_and_links(self):
        for player_to in self.get_players():
            for player_from in self.get_players():
                kiubo_prop_from = False
                kiubo_link = 0
                if player_from.name != player_to.name: # si no soy yo mismo
                    kiubo_prop_from = bool(getattr(player_from, 'prop_to_' + player_to.name)) # cojo el valor de la propuesta
                    if getattr(player_to, 'prop_to_' + player_from.name) == True and kiubo_prop_from == True:
                        kiubo_link = 1
                    else:
                        kiubo_link = 0
                else:
                    kiubo_link = 0 # link conmigo mismo = 1

                setattr(player_to, 'prop_from_' + player_from.name, kiubo_prop_from) # la añado a prop_from_X
                setattr(player_to, 'link_with_' + player_from.name, kiubo_link)

    def calculate_degree(self):
        for player in self.get_players():
            player.out_degree = player.prop_to_1 + player.prop_to_2 + player.prop_to_3 + player.prop_to_4 + player.prop_to_5\
                                + player.prop_to_6 + player.prop_to_7
            player.degree = player.link_with_1 + player.link_with_2 + player.link_with_3 + player.link_with_4 + player.link_with_5 + \
                            player.link_with_6 + player.link_with_7

    def linking_costs(self):
        for player in self.get_players():
            player.linking_costs = player.out_degree * Constants.link_cost

    def calculate_actions(self):
        for player in self.get_players():
            for partner in self.get_players():
                action_up = partner.action
                if action_up == 1:
                    choice = 1
                else:
                    choice = 0
                setattr(player, 'action_' + partner.name, choice) # la añado a prop_from_X

    def sum_coordinations(self):
        for player in self.get_players():
            if player.action == player.action_1 and player.link_with_1 == 1:
                player.coordinate_1 = 1
            else:
                player.coordinate_1 = 0
            if player.action == player.action_2 and player.link_with_2 == 1:
                player.coordinate_2 = 1
            else:
                player.coordinate_2 = 0
            if player.action == player.action_3 and player.link_with_3 == 1:
                player.coordinate_3 = 1
            else:
                player.coordinate_3 = 0

            if player.action == player.action_4 and player.link_with_4 == 1:
                player.coordinate_4 = 1
            else:
                player.coordinate_4 = 0
            if player.action == player.action_5 and player.link_with_5 == 1:
                player.coordinate_5 = 1
            else:
                player.coordinate_5 = 0
            if player.action == player.action_6 and player.link_with_6 == 1:
                player.coordinate_6 = 1
            else:
                player.coordinate_6 = 0
            if player.action == player.action_7 and player.link_with_7 == 1:
                player.coordinate_7 = 1
            else:
                player.coordinate_7 = 0

    def coordination_score(self):
        for player in self.get_players():
            player.coordination_score = Constants.personal + player.coordinate_1 + player.coordinate_2 + \
                                        player.coordinate_3 + player.coordinate_4 + player.coordinate_5 + \
                                        player.coordinate_6 + player.coordinate_7

    def values_coordination(self):
        for player in self.get_players():
            if player.action == player.liked_action:
                player.coordination_gains = player.coordination_score * Constants.liked_gain
            else:
                player.coordination_gains = player.coordination_score * Constants.disliked_gain

    def round_gains(self):
        for player in self.get_players():
            player.round_gains = player.coordination_gains - player.linking_costs

    def round_payoffs(self):
        for player in self.get_players():
            if self.subsession.round_number == self.session.vars['paying_round_2']:
                player.payoff = player.round_gains
            else:
                player.payoff = 0

    def summing_choices(self):
        players = self.get_players()
        action_up = [p.action for p in players]
        self.total_up = sum(action_up)
        self.total_down = len(Constants.names) - self.total_up


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3
    given_symbol = models.BooleanField()
    given_preference = models.BooleanField() # circle or triangle assigned exogenously
    given_type = models.IntegerField() # combination of symbol and preference
    chosen_type = models.IntegerField() # combination of symbol and preference
    was_circle = models.IntegerField()
    is_circle = models.IntegerField()
    action = models.IntegerField() # Reported belief on P3's verification
    old_action = models.IntegerField() # Reported belief on P3's verification
    liked_action = models.IntegerField()
    out_degree = models.IntegerField()
    degree = models.IntegerField()
    coordination_score = models.IntegerField()
    coordination_gains = models.IntegerField()
    linking_costs = models.IntegerField()
    round_gains = models.IntegerField()
    name = models.StringField()
    friends = models.LongStringField()
    position = models.IntegerField()


for i in Constants.names:
    Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))
    # Añado a Player las variables de propuestas con friendly names que luego rellenaremos
    Player.add_to_class('prop_to_' + i,  models.BooleanField(initial=0))
    Player.add_to_class('prop_from_' + i, models.BooleanField(initial=0))
    Player.add_to_class('link_with_' + i, models.IntegerField(initial=0))
    Player.add_to_class('action_' + i,  models.IntegerField(initial=0))
    Player.add_to_class('coordinate_' + i,  models.IntegerField(initial=0))

