from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.MyPage)
        yield (pages.Results)


    def play_round(self):
        yield (pages.WelcomeP2)
        yield (pages.GroupChangeInst,
               {'new_symbol': 3})

# otree test switch_inst_p2 --export=test_inst_p2