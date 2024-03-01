from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'Welcome'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
# FUNCTIONS


# PAGES
class Welcome(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


page_sequence = [Welcome]
