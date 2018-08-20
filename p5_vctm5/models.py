from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
import csv


author = 'Manu Munoz-Herrera'

doc = """
Web of Lies p5_vctm5
"""


class Constants(BaseConstants):
    name_in_url = 'MTurk_p5_vctm5'
    players_per_group = None
    num_rounds = 1
    exchange_rate=c(3)
    belief_pay=c(20)
    min_report = 1
    max_report = 30
    num_blocks = 144
    instructions_template= 'p5_vctm5/Instructions.html'
    instructions_beliefs = 'p5_vctm5/InstructionsBeliefs.html'
    instructions_belief_number = 'p5_vctm5/Instbeliefnumber.html'
    instructions_belief_hiddennumber = 'p5_vctm5/Instbeliefhiddennumber.html'
    instructions_belief_yesno = 'p5_vctm5/Instbeliefyesno.html'
    exo_prob_show = 80 # Complete for EXO once ENDO is conducted
    exo_prob_no_show = 20 # Complete for EXO once ENDO is conducted
    payment_days = 30
    show_up_fee = 1
    total_pay = 2.70

    with open('p5_vctm5/imp_p5_vctm5_c.csv', 'r') as f:
        reader = csv.reader(f)
        data_player1 = list(reader)

class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1,2,3,4,5,11])
            # for p in self.get_players():
            #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Treat. 1: FRST3, 2: NO3, 3:EXO3, 4:ENDO3, 5:VCTM3 11: VCTM5
    treat = models.IntegerField() # Treatments from 6 to 10
    rnum = models.IntegerField(min=Constants.min_report, max=Constants.max_report)
    pnum = models.IntegerField(min=Constants.min_report, max=Constants.num_blocks)
    report_1 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 1
    report_2 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 2
    report_3 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 3
    exo_click = models.IntegerField() # Player 3 verifies
    endo_click = models.BooleanField() # Player 3 verifies
    random_show = models.IntegerField() # Randomly generated number
    inst_show = models.BooleanField(blank=True,)
    correct = models.IntegerField() # Use it as conditional to show or skip screens and end the game
    belief1 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P1's choices
    belief2 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P2's choices
    belief3 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P3's choices
    belief_endo= models.BooleanField() # Reported belief on P3's verification
    random_group = models.BigIntegerField()
    player_role = models.IntegerField()
    duplicate = models.IntegerField()

    def assigning_values(self):
        self.random_group = int(Constants.data_player1[self.id_in_group][4])
        self.rnum = int(Constants.data_player1[self.id_in_group][5])
        self.report_1 = int(Constants.data_player1[self.id_in_group][6])
        self.report_2 = int(Constants.data_player1[self.id_in_group][7])
        self.report_3 = int(Constants.data_player1[self.id_in_group][8])
        self.player_role = 5
        self.duplicate = int(Constants.data_player1[self.id_in_group][9])

    gender = models.PositiveIntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other']
        ],
        widget=widgets.RadioSelect
    )

    ethnicity = models.PositiveIntegerField(
        choices=[
            [1, 'Hispanic / Latino / Latina'],
            [2, 'Not Hispanic / Latino / Latina'],
        ],
        widget=widgets.RadioSelect
    )

    race = models.PositiveIntegerField(
        choices=[
            [1, 'White'],
            [2, 'Black / African American'],
            [3, 'Asian'],
            [4, 'American Indian / Alaskan Native'],
            [5, 'Middle Eastern / North African'],
            [6, 'Native Hawaiian / Pacific Islander'],
            [7, 'Other']
        ],
        widget=widgets.RadioSelect
    )

    age = models.IntegerField (min=18, max=100)

    education = models.PositiveIntegerField(
        choices=[
            [1, 'Less than high school'],
            [2, 'High school diploma or equivalent (e.g., GED)'],
            [3, 'Some college'],
            [4, 'College diploma'],
            [5, 'Masters degree'],
            [6, 'Professional post-secondary degree or doctoral degree (e.g., JD, MD, PhD etc.)'],
        ],
        widget=widgets.RadioSelect
    )


    state = models.PositiveIntegerField(
        choices=[
            [1, ' Alabama '],
            [2, ' Alaska '],
            [3, ' Arizona '],
            [4, ' Arkansas '],
            [5, ' California '],
            [6, ' Colorado '],
            [7, ' Connecticut '],
            [8, ' Delaware '],
            [9, ' District of Columbia '],
            [10, ' Florida '],
            [11, ' Georgia '],
            [12, ' Hawaii '],
            [13, ' Idaho '],
            [14, ' Illinois '],
            [15, ' Indiana '],
            [16, ' Iowa '],
            [17, ' Kansas '],
            [18, ' Kentucky '],
            [18, ' Louisiana '],
            [19, ' Maine '],
            [20, ' Maryland '],
            [21, ' Massachusetts '],
            [22, ' Michigan '],
            [23, ' Minnesota '],
            [24, ' Mississippi '],
            [25, ' Missouri '],
            [26, ' Montana '],
            [27, ' Nebraska '],
            [28, ' Nevada '],
            [29, ' New Hampshire '],
            [30, ' New Jersey '],
            [31, ' New Mexico '],
            [32, ' New York '],
            [33, ' North Carolina '],
            [34, ' North Dakota '],
            [35, ' Ohio '],
            [36, ' Oklahoma '],
            [37, ' Oregon '],
            [38, ' Pennsylvania '],
            [39, ' Rhode Island '],
            [40, ' South Carolina '],
            [41, ' South Dakota '],
            [42, ' Tennessee '],
            [43, ' Texas '],
            [44, ' Utah '],
            [45, ' Vermont '],
            [46, ' Virginia '],
            [47, ' Washington '],
            [48, ' Washington DC'],
            [49, ' West Virginia '],
            [50, ' Wisconsin '],
            [51, ' Wyoming '],
        ],
    )

    income = models.PositiveIntegerField(
        choices=[
            [1, 'Less than $10,000'],
            [2, '$10,000 - $19,999'],
            [3, '$20,000 - $29,999'],
            [4, '$30,000 - $39,999'],
            [5, '$40,000 - $49,999'],
            [6, '$50,000 - $59,999'],
            [7, '$60,000 - $69,999'],
            [8, '$70,000 - $79,999'],
            [9, '$80,000 - $99,999'],
            [10, '$100,000 - $119,999'],
            [11, '$120,000 - $149,999'],
            [12, '$150,000 - $199,999'],
            [13, '$200,000 -'],
            [14, 'I do not wish to report my income.'],
        ],
        widget=widgets.RadioSelect
    )

    distribution = models.IntegerField(
        choices=[
            [0, '10'],
            [1, '4'],
            [2, '25'],
            [3, '18'],
            [4, '20'],
        ],
        widget=widgets.RadioSelect
    )

    infop2  = models.PositiveIntegerField(blank=True,
        choices=[
            [0, "P2 will see the number reported by P1, and with {}% chance will also see the hidden number".format(Constants.exo_prob_show)],
            [1, 'P2 will see the number reported by P1 and will see the hidden number if he/she clicks on a button so that it shows on the screen'],
            [2, 'P2 will see the number reported by P1 but not the hidden number'],
            [3, 'P2 will not see the number reported by P1, only the hidden number'],
            [4, 'P2 will not see any messages, he/she is a passive player'],
        ],
        widget=widgets.RadioSelect
    )

    infop3  = models.PositiveIntegerField(blank=True,
        choices=[
            [0, "P3 will see the number reported by P2, and with {}% chance will also see the hidden number".format(Constants.exo_prob_show)],
            [1, 'P3 will see the number reported by P2 and will see the hidden number if he/she clicks on a button so that it shows on the screen'],
            [2, 'P3 will see the number reported by P2 but not the hidden number'],
            [3, 'P3 will not see the number reported by P2, only the hidden number'],
            [4, 'P3 will not see any messages, he/she is a passive player'],
        ],
        widget=widgets.RadioSelect
    )


    earnings1 = models.IntegerField(
        choices=[
            [0, ' 24x5 = 120 cents'],
            [1, '  6x5 = 30 cents'],
            [2, ' 12x5 = 60 cents'],
            [3, ' 18x5 = 90 cents'],
            [4, 'It cannot be determined from this information alone'],
        ],
        widget=widgets.RadioSelect
    )

    earnings2 = models.IntegerField(
        choices=[
            [0, ' 24x5 = 120 cents'],
            [1, '  6x5 = 30 cents'],
            [2, ' 12x5 = 60 cents'],
            [3, ' 18x5 = 90 cents'],
            [4, 'It cannot be determined from this information alone'],
        ],
        widget=widgets.RadioSelect
    )

    earnings4a = models.IntegerField(blank=True,
        choices=[
            [0, ' (2x12)x5 = 120 cents'],
            [1, ' (2x12-18)x5 = 30 cents'],
            [2, ' (2x12-12)x5 = 60 cents'],
            [3, ' (18x5) = 90 cents'],
            [4, 'It cannot be determined from this information alone'],
        ],
        widget=widgets.RadioSelect
    )

    earnings4b = models.IntegerField(blank=True,
        choices=[
            [0, ' (2x12)x5 = 120 cents'],
            [1, ' (2x12-18)x5 = 30 cents'],
            [2, ' (2x12-12)x5 = 60 cents'],
            [3, ' (18x5) = 90 cents'],
            [4, 'It cannot be determined from this information alone'],
        ],
        widget=widgets.RadioSelect
    )

    pretest1 = models.LongStringField()
    pretest2 = models.IntegerField(
        choices=[
            [1, '1. Extremely Positive'],
            [2, '2. Very Positive'],
            [3, '3. Positive'],
            [4, '4. Neutral'],
            [5, '5. Negative'],
            [6, '6. Very Negative'],
            [7, '7. Extremely Negative'],
        ],
        widget = widgets.RadioSelect
    )
    pretest3 = models.LongStringField()

    def set_payoffs(self):
        self.payoff = (self.report_3)