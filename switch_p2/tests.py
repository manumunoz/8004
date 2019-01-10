from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Type)

        if self.player.treat == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([1, 5])})
        elif self.player.treat == 2 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([1, 2])})
        elif self.player.treat == 2 and self.player.given_type == 4:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([5, 6])})
        elif self.player.treat == 3 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([3, 4])})
        elif self.player.treat == 3 and self.player.given_type == 4:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([7, 8])})

        decisions = {}
        for p in self.player.get_others_in_group():
            decisions[p.name] = random.choice([False, True])

        yield pages.Formation, decisions

        yield (pages.Action,
               {'action': random.choice([0, 1])})

        yield (pages.Results)

        # if self.round_number == 10:
        #     yield (pages.RandomPay)

# otree test switch_p2_t2 --export=switch_p2_test

# otree test sticky_en --export=test_sticky_en