import random
from otree.api import *
from TREATMENT_CONFIG import *


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = 2
    num_rounds = 1
    discount = 0.7
    treatment = TREATMENT


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dictator_do = models.IntegerField(initial=0)   # =1 pay, =0 not pay


class Player(BasePlayer):

    f_int1 = models.IntegerField(initial=2)
    f_int2 = models.IntegerField(initial=0)
    f_int3 = models.IntegerField(initial=3)
    f_int4 = models.IntegerField(initial=4)
    f_int5 = models.IntegerField(initial=0)
    f_int6 = models.IntegerField(initial=3)
    f_int7 = models.IntegerField(initial=2)
    f_int8 = models.IntegerField(initial=4)
    f_int9 = models.IntegerField(initial=3)
    f_int10 = models.IntegerField(initial=1)
    f_int11 = models.IntegerField(initial=4)
    f_int12 = models.IntegerField(initial=2)
    f_int13 = models.IntegerField(initial=1)
    f_int14 = models.IntegerField(initial=1)
    f_int15 = models.IntegerField(initial=1)
    f_int16 = models.IntegerField(initial=3)

    final_tokens = models.FloatField()
    # Demographics
    gender = models.StringField(
        choices=[['男', '男'], ['女', '女']],
        label='你的性别',
        widget=widgets.RadioSelectHorizontal)

    age = models.IntegerField(
        label='你的年龄',
        min=15, max=70)

    grade = models.IntegerField(
        label='你的年级是',
        choices=[[1, '大一'], [2, '大二'], [3, '大三'], [4, '大四及以上']],
        widget=widgets.RadioSelectHorizontal)

    major = models.StringField(
        label='你现在的专业是')

    huji = models.StringField(
        choices=[['农村', '农村'], ['城市', '城市']],
        label='你的户籍所在地是',
        widget=widgets.RadioSelect)

    father_edu = models.StringField(
        choices=[['小学', '小学'], ['初中', '初中'], ['高中', '高中'], ['专科教育', '专科教育'],
                 ['本科教育', '本科教育'], ['研究生教育', '研究生教育']],
        label='你的父亲的最高学历是',
        widget=widgets.RadioSelect)

    mother_edu = models.StringField(
        choices=[['小学', '小学'], ['初中', '初中'], ['高中', '高中'], ['专科教育', '专科教育'],
                 ['本科教育', '本科教育'], ['研究生教育', '研究生教育']],
        label='你的母亲的最高学历是',
        widget=widgets.RadioSelect)

    fam_inc = models.IntegerField(label='你的家庭人均年收入是多少元',)

    expenditure = models.IntegerField(
        label='你每个月的生活费为多少',
        choices=[[1000, '1000元以下'], [1250, '1000-1500元'], [1750, '1500-2000元'], [2250, '2000-2500元'],
                 [2500, '2500元以上']],
        widget=widgets.RadioSelectHorizontal)

    software = models.StringField(
        choices=[['未下载过', '未下载过'], ['下载过，老师/朋友/同学传给我', '下载过，老师/朋友/同学传给我'],
                 ['下载过，自己在网上免费查找到', '下载过，自己在网上免费查找到'], ['下载过，在网上非官方渠道购得', '下载过，在网上非官方渠道购得']
            , ['下载过，在官方渠道购得', '下载过，在官方渠道购得']],
        label='你是否下载过Stata、Eviews、SPSS等学习软件？如果是，你主要的下载途径是？',
        widget=widgets.RadioSelect)

    books = models.StringField(
        choices=[['未下载过', '未下载过'], ['下载过，老师/朋友/同学传给我', '下载过，老师/朋友/同学传给我'],
                 ['下载过，自己在网上免费查找到', '下载过，自己在网上免费查找到'], ['下载过，在网上非官方渠道购得', '下载过，在网上非官方渠道购得']
            , ['下载过，在官方渠道购得', '下载过，在官方渠道购得']],
        label='你是否使用过电子版教材？如果是，你主要的下载途径是？',
        widget=widgets.RadioSelect)

    onlychild = models.StringField(
        choices=[['独生', '独生'], ['非独生', '非独生']],
        label='你是否是独生子女？',
        widget=widgets.RadioSelectHorizontal)

    minority = models.StringField(
        choices=[['少数民族', '少数民族'], ['汉族', '汉族']],
        label='你是否是少数民族？',
        widget=widgets.RadioSelectHorizontal)

    cpc = models.StringField(
        choices=[['中共党员', '中共党员'], ['预备党员', '预备党员'], ['入党积极分子', '入党积极分子'], ['共青团员', '共青团员'], ['其他', '其他']],
        label='你的政治面貌？',
        widget=widgets.RadioSelectHorizontal)

    leader = models.StringField(
        choices=[['是', '是'], ['不是', '不是']],
        label='你是否是学生干部（班干部、学生会、团委等）',
        widget=widgets.RadioSelectHorizontal)

    # strategy = models.StringField(
    #     label='你选择告知同组参与者A文本转换任务价格/收益的策略是什么：', initial=" ")

    dictator = models.IntegerField(
        label='（你需要进行如下决策，你在本问中的决策有20%的概率兑现并获得真实收益，然后50%的概率是分配者，50%的概率是接受者）'
              '本阶段中，若你填写问卷获得了10实验币，你希望交给同组实验者实验币的数量为：',
        min=0, max=10
    )
    pizza = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[-3, -2, -1, 0, 1, 2, 3]
    )


# FUNCTIONS
def creating_session(subsession):
    import random
    subsession.group_randomly()
    for g in subsession.get_groups():
        rand = random.randint(1, 10)
        # print(rand)
        if rand <= 12:
            g.dictator_do = 1
        else:
            g.dictator_do = 0


def calculate_final_tokens(subsession):
    for p in subsession.get_players():
        if p.group.dictator_do == 1:
            if p.id_in_group == 1:
                p.final_tokens = p.participant.tokens + (10 - p.dictator) + 10
            else:
                p.final_tokens = p.participant.tokens + p.group.get_player_by_id(1).dictator + 10
        else:
            p.final_tokens = p.participant.tokens + 10

        p.payoff = p.final_tokens * Constants.discount


# PAGES
class Question(Page):
    form_model = 'player'
    form_fields = [
        'f_int1', 'f_int2', 'f_int3', 'f_int4','f_int5','f_int6','f_int7','f_int8','f_int9','f_int10','f_int11','f_int12',
        'f_int13','f_int14','f_int15','f_int16',
    ]
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


class DemographicsA(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'grade', 'major', 'huji', 'father_edu', 'mother_edu', 'fam_inc', 'expenditure',
                   'software', 'books',
                   'onlychild', 'minority', 'cpc', 'leader',
                   ]

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


class DG(Page):
    form_model = 'player'
    form_fields = ['dictator']

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


# class DemographicsB(Page):
#     form_model = 'player'
#     form_fields = ['gender', 'age', 'grade', 'major', 'huji', 'father_edu', 'mother_edu', 'fam_inc', 'expenditure',
#                    'software', 'books',
#                    'onlychild', 'minority', 'cpc', 'leader',  'dictator'
#                    ]
#
#     @staticmethod
#     def is_displayed(player):
#         return player.id_in_group == 2 and player.round_number == Constants.num_rounds


class WaitPage6(WaitPage):
    wait_for_all_groups = True
    body_text = "请等待所有参与者完成决策，即将进入最终结果页面。"

    def after_all_players_arrive(subsession: Subsession):
        calculate_final_tokens(subsession)

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds



    @staticmethod
    def vars_for_template(player):
        player_b_price = player.participant.p2price
        return {'player_a_see': player_b_price,
                'b_return': 20 - player_b_price,
                'dictator_give': player.group.get_player_by_id(1).dictator,
                'b_return_profit': player_b_price - 10,
                'b_gain': 30-player_b_price,
                }


page_sequence = [DG, Question,
                 DemographicsA, WaitPage6, Results
                 ]
