from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Welcome)

        yield (pages.Sociodemo,
               {'gender': random.randint(1, 3), 'ethnicity': random.randint(1, 2), 'race': random.randint(1, 7),
                'age': 22, 'education': 1, 'state': 1, 'income': 1})

        yield (pages.Start)

        yield (pages.Comprehension, {'distribution': 0, 'infop2': 4, 'earnings1': 2, 'earnings2': 3})

        yield (pages.NoReport)

        yield (pages.Beliefintro)

        yield (pages.Beliefsa, {'belief1': random.randint(1, 30)})

        yield (pages.Pretest, {'pretest1': 0, 'pretest2': 1, 'pretest3': 101})

# otree test p3_frst3 --export=test_p3_frst3
