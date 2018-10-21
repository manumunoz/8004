from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.ChosenType,
               {'chosen_type':random.choice([1, 4])})

        decisions = {}
        for p in self.player.get_others_in_group():
            decisions[p.name] = random.randint(0, 1)

        yield pages.Formation, decisions

        yield (pages.Action,
               {'action': random.randint(0,1)})

        yield (pages.Results)

# otree test switch_p2 --export=switch_p2_test

# otree test full_switch --export=full_switch_test