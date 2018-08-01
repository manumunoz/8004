from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
import csv


author = 'Manu Munoz-Herrera'

doc = """
Web of Lies 3-player: Player 4
"""


class Constants(BaseConstants):
    name_in_url = 'MTurk_3Study_P4'
    players_per_group = None
    num_rounds = 1
    exchange_rate=c(3)
    belief_pay=c(20)
    min_report = 1
    max_report = 30
    num_blocks = 144
    instructions_template= 'three_p4/Instructions.html'
    instructions_beliefs = 'three_p4/InstructionsBeliefs.html'
    instructions_belief_number = 'three_p4/Instbeliefnumber.html'
    instructions_belief_hiddennumber = 'three_p4/Instbeliefhiddennumber.html'
    instructions_belief_yesno = 'three_p4/Instbeliefyesno.html'
    exo_prob_show = 80 # Complete for EXO once ENDO is conducted
    exo_prob_no_show = 20 # Complete for EXO once ENDO is conducted

    # imp_rnum_T1 = [1,1,1,1,1,1] # Update after P1
    # imp_rnum_T2 = [2,2,2,2,2,2] # Update after P1
    # imp_rnum_T3 = [3,3,3,3,3,3] # Update after P1
    # imp_rnum_T4 = [4,4,4,4,4,4] # Update after P1
    imp_rnum_T5 = [5,5,5,5,5,5] # Update after P1
    imp_rnum_T11 = [11,11,11,11,11,11] # Update after P1
    # imp_rnum_T6 = [6,6,6,6,6,6] # Update after P1
    # imp_rnum_T7 = [7,7,7,7,7,7] # Update after P1
    # imp_rnum_T8 = [8,8,8,8,8,8] # Update after P1
    # imp_rnum_T9 = [9,9,9,9,9,9] # Update after P1
    # imp_rnum_T10 = [10,10,10,10,10,10] # Update after P1

    # imp_report1_T1 = [1,1,1,1,1,1] # Update after P1
    # imp_report1_T2 = [2,2,2,2,2,2] # Update after P1
    # imp_report1_T3 = [3,3,3,3,3,3] # Update after P1
    # imp_report1_T4 = [4,4,4,4,4,4] # Update after P1
    imp_report1_T5 = [5,5,5,5,5,5] # Update after P1
    imp_report1_T11 = [11,11,11,11,11,11] # Update after P1
    # imp_report1_T6 = [6,6,6,6,6,6] # Update after P1
    # imp_report1_T7 = [7,7,7,7,7,7] # Update after P1
    # imp_report1_T8 = [8,8,8,8,8,8] # Update after P1
    # imp_report1_T9 = [9,9,9,9,9,9] # Update after P1
    # imp_report1_T10 = [10,10,10,10,10,10] # Update after P1

    # imp_report2_T1 = [1,1,1,1,1,1] # Update after P1
    # imp_report2_T2 = [2,2,2,2,2,2] # Update after P1
    # imp_report2_T3 = [3,3,3,3,3,3] # Update after P1
    # imp_report2_T4 = [4,4,4,4,4,4] # Update after P1
    imp_report2_T5 = [5,5,5,5,5,5] # Update after P1
    imp_report2_T11 = [11,11,11,11,11,11] # Update after P1
    # imp_report2_T6 = [6,6,6,6,6,6] # Update after P1
    # imp_report2_T7 = [7,7,7,7,7,7] # Update after P1
    # imp_report2_T8 = [8,8,8,8,8,8] # Update after P1
    # imp_report2_T9 = [9,9,9,9,9,9] # Update after P1
    # imp_report2_T10 = [10,10,10,10,10,10] # Update after P1

class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([5,11])
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
    treat = models.IntegerField() # Treatments from 1 to 5 & 11
    rnum = models.IntegerField(min=Constants.min_report, max=Constants.max_report)
    pnum = models.IntegerField(min=Constants.min_report, max=Constants.num_blocks)
    report_1 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 1
    report_2 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 2
    report_3 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Choice player 3
    exo_click = models.BooleanField() # Player 3 verifies
    endo_click = models.BooleanField() # Player 3 verifies
    random_show = models.IntegerField() # Randomly generated number
    inst_show = models.BooleanField(blank=True,)
    correct = models.BooleanField() # Use it as conditional to show or skip screens and end the game
    belief1 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P1's choices
    belief2 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P2's choices
    belief3 = models.IntegerField(min=Constants.min_report, max=Constants.max_report) # Reported belief on P3's choices
    belief_endo= models.BooleanField() # Reported belief on P3's verification

    def assigning_values(self):
        if self.treat == 1:
            self.rnum = Constants.imp_rnum_T1[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T1[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T1[self.id_in_group - 1] #This is to test. It must be replaced before running the session
        elif self.treat == 2:
            self.rnum = Constants.imp_rnum_T2[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T2[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T2[self.id_in_group - 1] #This is to test. It must be replaced before running the session
        elif self.treat == 3:
            self.rnum = Constants.imp_rnum_T3[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T3[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T3[self.id_in_group - 1] #This is to test. It must be replaced before running the session
        elif self.treat == 4:
            self.rnum = Constants.imp_rnum_T4[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T4[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T4[self.id_in_group - 1] #This is to test. It must be replaced before running the session
        elif self.treat == 5:
            self.rnum = Constants.imp_rnum_T5[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T5[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T5[self.id_in_group - 1] #This is to test. It must be replaced before running the session
        else:
            self.rnum = Constants.imp_rnum_T11[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_1 = Constants.imp_report1_T11[self.id_in_group - 1] #This is to test. It must be replaced before running the session
            self.report_2 = Constants.imp_report2_T11[self.id_in_group - 1] #This is to test. It must be replaced before running the session

    def random_display(self):
        self.random_show = random.randint(1, 100)
        if self.round_number <= Constants.exo_prob_show:
            self.exo_click = 1
        else:
            self.exo_click = 0

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