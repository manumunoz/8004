from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.assigning_values()
        self.player.random_display()

class Sociodemo(Page):
    form_model = 'player'
    form_fields = ['gender', 'ethnicity', 'race', 'age', 'education', 'state', 'income']

    def age_error_message(self, value):
        is_correct = (value >= 18)
        if not (is_correct):
            return 'You must be at least 18 years old to participate in this study.'

class Start(Page):
    pass

class Comprehension(Page):
    form_model = 'player'
    form_fields = ['distribution', 'infop2', 'infop3', 'earnings1', 'earnings2', 'earnings4a', 'earnings4b']


    def before_next_page(self):
        if self.player.distribution == 0 and self.player.infop2 == 4 and \
                self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 1:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==2 \
                and self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 2:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==0 and \
                self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 3:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 4:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings4a == 2 and self.player.earnings2==3 and \
                self.player.earnings4b == 1 and self.player.treat == 5:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings4a == 2 and self.player.earnings2==3 and \
                self.player.earnings4b == 1 and self.player.treat == 11:
            self.player.correct = 1
        else:
            self.player.correct = 0

class Comprehension2(Page):
    def is_displayed(self):
        return self.player.correct == 0

    form_model = 'player'
    form_fields = ['distribution', 'infop2', 'infop3', 'earnings1', 'earnings2', 'earnings4a', 'earnings4b']

    def before_next_page(self):
        if self.player.distribution == 0 and self.player.infop2 == 4 and \
                self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 1:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==2 \
                and self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 2:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==0 and \
                self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 3:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings2==3 and self.player.treat == 4:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings4a == 2 and self.player.earnings2==3 and \
                self.player.earnings4b == 1 and self.player.treat == 5:
            self.player.correct = 1
        elif self.player.distribution == 0 and self.player.infop2 == 2 and self.player.infop3==1 and \
            self.player.earnings1==2 and self.player.earnings4a == 2 and self.player.earnings2==3 and \
                self.player.earnings4b == 1 and self.player.treat == 11:
            self.player.correct = 1
        else:
            self.player.correct = 0

class NoReport(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

class Beliefintro(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

class Beliefsa(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

    form_model = 'player'
    form_fields = ['belief1']

class Beliefsab(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

    form_model = 'player'
    form_fields = ['belief2']

class Beliefsendo(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

    form_model = 'player'
    form_fields = ['belief_endo']

class Beliefsb(Page):
    def is_displayed(self):
        return self.player.correct == 1 and self.player.treat >= 5

    form_model = 'player'
    form_fields = ['belief3']

    def before_next_page(self):
        self.player.set_payoffs()

class Pretest(Page):
    def is_displayed(self):
        return self.player.correct == 1

    form_model = 'player'
    form_fields = ['pretest1','pretest2','pretest3']

    def before_next_page(self):
        self.player.set_payoffs()

class Pass(Page):
    def is_displayed(self):
        return self.player.correct == 1

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }

class NoPass(Page):
    def is_displayed(self):
        return self.player.correct == 0

page_sequence = [
    Welcome,
    Sociodemo,
    Start,
    Comprehension,
    Comprehension2,
    NoReport,
    Beliefintro,
    Beliefsa,
    Beliefsab,
    Beliefsendo,
    Beliefsb,
    Pretest,
    Pass,
    NoPass,
]
