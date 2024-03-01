import random
from otree.api import *
from TREATMENT_CONFIG import *


class Constants(BaseConstants):
    name_in_url = 'CostProfit0426'
    players_per_group = 2
    num_rounds = 1
    discount = 1
    treatment = TREATMENT   # from TREATMENT_CONFIG


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # dictator_do = models.IntegerField(initial=0)   # =1 pay, =0 not pay
    pass



class Player(BasePlayer):
    count_task1 = models.IntegerField()  # count 0 task question 1
    count_task2 = models.IntegerField()
    count_task3 = models.IntegerField()
    count_task4 = models.IntegerField()
    count_task5 = models.IntegerField()
    count_task6 = models.IntegerField()
    count_task7 = models.IntegerField()
    count_task8 = models.IntegerField()
    count_task9 = models.IntegerField()
    count_task10 = models.IntegerField()

    norm_income = models.IntegerField(initial=0)

    social_norm0 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm1 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm2 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm3 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm4 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm5 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm6 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm7 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm8 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm9 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    social_norm10 = models.StringField(
        choices=[['符合社会规范', '符合社会规范'], ['比较符合社会规范', '比较符合社会规范'], ['比较不符合社会规范', '比较不符合社会规范'],
                 ['不符合社会规范', '不符合社会规范']],
        label='',
        widget=widgets.RadioSelectHorizontal,
        initial='不适用')

    account = models.IntegerField(initial=0)  # account
    price = models.IntegerField(label="", min=10, max=20)           # B tell the price to A

    transfer1 = models.IntegerField()  # transfer task question 1
    # transfer2 = models.IntegerField()
    # transfer3 = models.IntegerField()
    # transfer4 = models.IntegerField()
    # transfer5 = models.IntegerField()
    # transfer6 = models.IntegerField()
    # transfer7 = models.IntegerField()
    # transfer8 = models.IntegerField()
    # transfer9 = models.IntegerField()
    # transfer10 = models.IntegerField()

    a_guess_b = models.IntegerField(label="", min=10, max=20)
    guess_prices = models.FloatField(label="", min=10, max=20)
    guess_guesses = models.IntegerField(label="", min=10, max=20)

    guess_correct = models.FloatField(initial=0, label="")
    guess_correct2 = models.FloatField(initial=0, label="")

    tokens = models.FloatField(initial=0)
    right_side_amount = models.IntegerField(initial=10)
    switching_point = models.IntegerField(initial=0)
    loss_A_num = models.IntegerField(initial=0)
    loss_B_num = models.IntegerField(min=0, max=11)
    loss_yes = models.IntegerField(initial=0)
    loss_which = models.IntegerField(initial=0)
    loss_token = models.FloatField(initial=0)

    guess_loss = models.FloatField(label="", min=0, max=11)
    guess_loss_correct = models.IntegerField(initial=0)
    social_norm = models.FloatField(label="", min=10, max=20 )

# FUNCTIONS
# def creating_session(subsession):
#     import random
#     for g in subsession.get_groups():
#         rand = random.randint(1, 10)
#         # print(rand)
#         if rand <= 2:
#             g.dictator_do = 1
#         else:
#             g.dictator_do = 0


def determine_loss_tokens(subsession):
    for p in subsession.get_players():
        p.loss_which = random.randint(1, 11)   # which task to decide loss
        p.loss_yes = random.choice([1, 0])     # whether lose in loss task
        if p.loss_which <= (p.switching_point - 10) / 2:
            loss_get = 0
        else:
            if p.loss_which == 1:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 10
            elif p.loss_which == 2:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 12
            elif p.loss_which == 3:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 14
            elif p.loss_which == 4:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 16
            elif p.loss_which == 5:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 18
            elif p.loss_which == 6:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 20
            elif p.loss_which == 7:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 22
            elif p.loss_which == 8:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 24
            elif p.loss_which == 9:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 26
            elif p.loss_which == 10:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 28
            else:
                if p.loss_yes == 1:
                    loss_get = -10
                else:
                    loss_get = 30
        p.loss_token = round(float(loss_get), 2)

        p.participant.vars['loss_yes'] = p.loss_yes
        p.participant.vars['loss_which'] = p.loss_which
        p.participant.vars['loss_token'] = p.loss_token
        p.participant.vars['loss_A_num'] = int((p.switching_point - 10) / 2)

def cordination_norm(subsession):
    for player in subsession.get_players():
        player.norm_income = 0
        import random
        for group in subsession.get_groups():
        # 获取 id 为 2 的所有参与者
            players_with_id_2 = [player for player in group.get_players() if player.id_in_group == 2]

        # 如果这样的参与者存在，从中随机选择一个
            if players_with_id_2:
                selected_player = random.choice(players_with_id_2)
                # 现在你可以对 selected_player 执行你想要的操作
                i = random.randint(0, 10)
                var_name = f'social_norm{i}'
            if player.id_in_group == 2:
                player_var_value = getattr(player, var_name)
                selected_player_var_value = getattr(selected_player, var_name)
                if player_var_value == selected_player_var_value:
                    player.norm_income = 3
            if player.id_in_group == 1 and (Constants.treatment != "T5" or Constants.treatment != "T6"):
                player_var_value = getattr(player, var_name)
                selected_player_var_value = getattr(selected_player, var_name)
                if player_var_value == selected_player_var_value:
                    player.norm_income = 3


def calculate_guess_tokens(subsession):
    b_players_prices = []
    for p in subsession.get_players():
        if p.id_in_group == 2:
            b_players_prices.append(p.price)
    for p in subsession.get_players():
        if Constants.treatment == "T1" or Constants.treatment == "T2"\
                or Constants.treatment == "T3" or Constants.treatment == "T4":
            if p.id_in_group == 1:
                if p.a_guess_b == p.group.get_player_by_id(2).price:
                    p.guess_correct = 1
                elif abs(p.a_guess_b - p.group.get_player_by_id(2).price) == 1:
                    p.guess_correct = 1/3
                else:
                    p.guess_correct = 0
            elif p.id_in_group == 2:
                all_b_prices_except_me = b_players_prices.copy()
                all_b_prices_except_me.remove(p.price)
                if len(all_b_prices_except_me) > 0:
                    avg = sum(all_b_prices_except_me) / len(all_b_prices_except_me)
                    if abs(p.guess_prices - avg) <= 0.5:
                        p.guess_correct = 1
                    elif (abs(p.guess_prices - avg) > 0.5) and (abs(p.guess_prices - avg) <= 1):
                        p.guess_correct = 1/3
                    else:
                        p.guess_correct = 0
                else:
                    p.guess_correct = 0
                if p.guess_guesses == p.group.get_player_by_id(1).a_guess_b:
                    p.guess_correct2 = 1
                elif abs(p.guess_guesses - p.group.get_player_by_id(1).a_guess_b) == 1:
                    p.guess_correct2 = 1/3
                else:
                    p.guess_correct2 = 0

        elif Constants.treatment == "T5" or Constants.treatment == "T6":
            if p.id_in_group == 1:
                p.guess_correct = 0
            elif p.id_in_group == 2:
                all_b_prices_except_me = b_players_prices.copy()
                all_b_prices_except_me.remove(p.price)
                if len(all_b_prices_except_me) > 0:
                    avg = sum(all_b_prices_except_me) / len(all_b_prices_except_me)
                    if abs(p.guess_prices - avg) <= 0.5:
                        p.guess_correct = 1
                    elif (abs(p.guess_prices - avg) > 0.5) and (abs(p.guess_prices - avg) <= 1):
                        p.guess_correct = 1/3
                    else:
                        p.guess_correct = 0
                else:
                    p.guess_correct = 0
                p.guess_correct2 = 0

        else:
            pass

    # players_loss_nums = []
    # for p in subsession.get_players():
    #     players_loss_nums.append(p.loss_A_num)


def calculate_tokens(subsession):
    for p in subsession.get_players():
        if Constants.treatment == "T2":
            if p.id_in_group == 1:
                p.tokens = 20 + 20 - p.group.get_player_by_id(2).price \
                                + p.guess_correct * 3 + p.loss_token + p.norm_income
            else:
                p.tokens = (20 + p.price) \
                                + p.guess_correct * 3 \
                                + p.guess_correct2 * 3 + p.loss_token + p.norm_income
        elif Constants.treatment == "T5":
            if p.id_in_group == 1:
                p.tokens = 20 + 20 - p.group.get_player_by_id(2).price \
                        + p.loss_token + p.norm_income
            else:
                p.tokens = (20 + p.price) \
                       + p.guess_correct * 3 \
                       + p.loss_token + p.norm_income
        elif Constants.treatment == "T6":
            if p.id_in_group == 1:
                p.tokens = 10 + p.group.get_player_by_id(2).price \
                                + p.loss_token + p.norm_income
            else:
                p.tokens = (50 - p.price) \
                                + p.guess_correct * 3 \
                                + p.loss_token + p.norm_income
        else:
            if p.id_in_group == 1:
                p.tokens = 10 + p.group.get_player_by_id(2).price \
                                + p.guess_correct * 3 + p.loss_token + p.norm_income
            else:
                p.tokens = (50 - p.price) \
                                + p.guess_correct * 3 \
                                + p.guess_correct2 * 3 + p.loss_token + p.norm_income


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

class Id_tell(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

class WaitPage1(WaitPage):
    wait_for_all_groups = True
    body_text = "请等待其他人进入该阶段"

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


class Count0AnB(Page):
    form_model = 'player'
    form_fields = ['count_task1', 'count_task2', 'count_task3', 'count_task4', 'count_task5',
                   'count_task6', 'count_task7', 'count_task8', 'count_task9', 'count_task10']

    def error_message(player, values):
        if values['count_task1'] != 14:
            return '第1题错误，请重新输入'
        elif values['count_task2'] != 9:
            return '第2题错误，请重新输入'
        elif values['count_task3'] != 17:
            return '第3题错误，请重新输入'
        elif values['count_task4'] != 11:
            return '第4题错误，请重新输入'
        elif values['count_task5'] != 10:
            return '第5题错误，请重新输入'
        elif values['count_task6'] != 12:
            return '第6题错误，请重新输入'
        elif values['count_task7'] != 17:
            return '第7题错误，请重新输入'
        elif values['count_task8'] != 14:
            return '第8题错误，请重新输入'
        elif values['count_task9'] != 16:
            return '第9题错误，请重新输入'
        elif values['count_task10'] != 14:
            return '第10题错误，请重新输入'
        else:
            pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.account = 20


class WaitPage2(WaitPage):
    wait_for_all_groups = False
    body_text = "请等待其他人完成任务"


class IntroA1(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 \
               and player.round_number == Constants.num_rounds


class IntroA(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 \
               and player.round_number == Constants.num_rounds

class Social_NormA(Page):
    form_model = 'player'
    form_fields = ['social_norm0', 'social_norm1', 'social_norm2', 'social_norm3', 'social_norm4', 'social_norm5',
                   'social_norm6', 'social_norm7', 'social_norm8', 'social_norm9', 'social_norm10',
                   ]
    @staticmethod
    def is_displayed(player):
            return player.id_in_group == 1 \
                   and player.round_number == Constants.num_rounds \
                   and (Constants.treatment == "T2" or Constants.treatment == "T4")

class Social_NormB(Page):
    form_model = 'player'
    form_fields = ['social_norm0', 'social_norm1', 'social_norm2', 'social_norm3', 'social_norm4', 'social_norm5',
                   'social_norm6', 'social_norm7', 'social_norm8', 'social_norm9', 'social_norm10',
                   ]
    @staticmethod
    def is_displayed(player):
            return player.id_in_group == 2 \
                   and player.round_number == Constants.num_rounds

class IntroB1(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 \
               and player.round_number == Constants.num_rounds


class IntroB(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 \
               and player.round_number == Constants.num_rounds

class NormOfA(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 \
                and player.round_number == Constants.num_rounds \
                and (Constants.treatment == "T2" or Constants.treatment == "T4")
    form_fields = ['social_norm']
    form_model = 'player'

class NormOfB(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 \
                and player.round_number == Constants.num_rounds
    form_fields = ['social_norm']
    form_model = 'player'

class WaitPage3(WaitPage):
    wait_for_all_groups = False
    body_text = "请等待同组其他参与者。"

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

class LossA(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(right_side_amounts=range(10, 32, 2))

class b4AnBsee(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

class AnBSee(Page):
    form_model = 'player'
    form_fields = ['transfer1',
                   ]
    #  'transfer2', 'transfer3', 'transfer4', 'transfer5',
    #  'transfer6', 'transfer7', 'transfer8', 'transfer9', 'transfer10'

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    # @staticmethod
    # def vars_for_template(player):
    #     player_b_price = player.group.get_player_by_id(2).price
    #     return {'player_a_see': player_b_price,
    #             'b_return': 20 - player_b_price,
    #             }

    def error_message(player, values):
        # if values['transfer1'] != 248189:
        #     return '第1题错误，请重新输入'
        if values['transfer1'] != 817188213:
            return '回答错误，请重新输入'
        # elif values['transfer3'] != 91716927189119:
        #     return '第3题错误，请重新输入'
        # elif values['transfer4'] != 1094922116189119:
        #     return '第4题错误，请重新输入'
        # elif values['transfer5'] != 911420142211691078:
        #     return '第5题错误，请重新输入'
        # elif values['transfer6'] != 211498178:
        #     return '第6题错误，请重新输入'
        # elif values['transfer7'] != 18821229:
        #     return '第7题错误，请重新输入'
        # elif values['transfer8'] != 421225189:
        #     return '第8题错误，请重新输入'
        # elif values['transfer9'] != 1622201371413:
        #     return '第9题错误，请重新输入'
        # elif values['transfer10'] != 188192717:
        #     return '第10题错误，请重新输入'
        else:
            pass


class WaitPage4(WaitPage):
    wait_for_all_groups = False
    body_text = "请等待同组其他参与者。"

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    # def after_all_players_arrive(group: Group):
    #     for p in group.get_players():
    #         if Constants.treatment == "T1" or Constants.treatment == "T5":
    #             if p.id_in_group == 1:
    #                 p.account = 20 - p.group.get_player_by_id(2).price
    #             else:
    #                 p.account = p.price
    #         else:
    #             if p.id_in_group == 1:
    #                 p.account = 10
    #             else:
    #                 p.account = 10


class AfterTransfer(Page):
    @staticmethod
    def is_displayed(player):
        return Constants.treatment == "T5" \
               and player.round_number == Constants.num_rounds


class DecisionANoGuess(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 \
               and player.round_number == Constants.num_rounds \
               and (Constants.treatment == "T5" or Constants.treatment == "T6")


class DecisionA(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 \
               and player.round_number == Constants.num_rounds \
               and (Constants.treatment == "T2" or Constants.treatment == "T4")
    form_model = 'player'
    form_fields = ['a_guess_b']


class DecisionB(Page):
    form_model = 'player'
    form_fields = ['price']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 \
               and player.round_number == Constants.num_rounds


class WaitPage5(WaitPage):
    wait_for_all_groups = False
    body_text = "请等待同组参与者完成决策。"

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def after_all_players_arrive(group: Group):
        for p in group.get_players():
            if Constants.treatment == "T5":
                if p.id_in_group == 1:
                    p.account = 20 - p.group.get_player_by_id(2).price
                else:
                    p.account = p.price
            else:
                if p.id_in_group == 1:
                    p.account = 10
                else:
                    p.account = 10
            # 这里可能要修改。


class ShowPrice(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1 and player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player):
        player_b_price = player.group.get_player_by_id(2).price
        return {'player_a_see': player_b_price,
                'b_return': 20 - player_b_price,
                }


class Belief(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 and player.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['guess_prices']

    @staticmethod
    def vars_for_template(player):
        player_b_price = player.group.get_player_by_id(2).price
        return {'player_a_see': player_b_price,
                'b_return': 20 - player_b_price,
                }


class Belief2(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2 and player.round_number == Constants.num_rounds\
               and (Constants.treatment == "T2" or Constants.treatment == "T4")

    form_model = 'player'
    form_fields = ['guess_guesses']

    @staticmethod
    def vars_for_template(player):
        player_b_price = player.group.get_player_by_id(2).price
        return {'player_a_see': player_b_price,
                'b_return': 20 - player_b_price,
                }


class LossAversion(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['loss_A_num', 'loss_B_num']

    def error_message(player, values):
        if values['loss_A_num'] != values['loss_B_num']:
            return '输入信息不一致，请阅读说明'
        else:
            pass


class LossGuess(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['guess_loss']


class WaitPage6(WaitPage):
    wait_for_all_groups = True
    body_text = "请等待所有参与者完成决策。"
    
    @staticmethod
    def after_all_players_arrive(subsession):
        cordination_norm(subsession)
        determine_loss_tokens(subsession)
        calculate_guess_tokens(subsession)
        calculate_tokens(subsession)
        for p in subsession.get_players():
            p.participant.vars['id_in_main_exp_group'] = p.id_in_group
            p.participant.vars['p2price'] = p.group.get_player_by_id(2).price
            p.participant.vars['guess_correct'] = p.guess_correct
            p.participant.vars['guess_correct2'] = p.guess_correct2
            p.participant.vars['tokens'] = p.tokens
            p.participant.vars['norm_income'] = p.norm_income

#
# class Demographics(Page):
#     form_model = 'player'
#     form_fields = ['gender', 'age', 'grade', 'major', 'expenditure', 'software', 'books',
#                    'onlychild', 'minority', 'cpc', 'leader', 'dictator',
#                    ]
#
#

#
# class Results(Page):
#     @staticmethod
#     def is_displayed(player):
#         return player.round_number == Constants.num_rounds
#
#     @staticmethod
#     def vars_for_template(player):
#         player_b_price = player.group.get_player_by_id(2).price
#         return {'player_a_see': player_b_price,
#                 'b_return': 20 - player_b_price,
#                 'player2_give': player.group.get_player_by_id(2).dictator
#                 }


page_sequence = [Introduction,
                 WaitPage1, Id_tell, Count0AnB, WaitPage2,
                 IntroA1, IntroA, IntroB1, IntroB, b4AnBsee,
                 AnBSee, DecisionANoGuess, DecisionA, DecisionB,
                 Belief, Belief2, Social_NormA, Social_NormB, LossA, WaitPage6
                 # Demographics, WaitPage5, Results
                 ]
