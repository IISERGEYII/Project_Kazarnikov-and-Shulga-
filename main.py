import logging
from flask import Flask, request, jsonify
from Logic.New_logic import Hero, The_Fallen_Guardian, The_Dark_Knight, The_Lich_King


class Game:
    def __init__(self):
        self.sessionStorage = {}
        self.completed_sections = 0
        self.equipment_is_taken = 0
        self.marten_spell = False
        self.completed_tavern = False
        self.completed_market = False
        self.completed_church = False
        self.powerful_spell = False
        self.not_coin_for_marten_spell = False
        self.purchased_items = {1: False, 2: False, 3: False, 4: False}
        self.dict_text_alice = {0: (
            'Добро пожаловать, отважный герой. Ты долго странствовал по диким землям, и вот — впереди город у подножия'
            ' мрачной горы. Над ним, как тень прошлого, возвышается древний замок, в чьих залах пробудился Король-Лич'
            ' — повелитель мёртвых. Его магия уже накрывает землю, и страх сковывает сердца людей.\n'
            ' \n'
            ''
            'Но надежда ещё жива — она в тебе. Только ты можешь взобраться на вершину, преодолеть опасности и сразить'
            ' Лича, пока не стало слишком поздно. И помни - каждая история заканчивается чтобы начаться заново.\n'
            ' \n'
            'Готов ли ты вступить в это приключение?(Введите цифру варианта вашего ответа, чтобы продолжить)\n'
        ),

            1: (
                'Только ты сделал шаг на пыльную дорогу, ведущую к городу, как воздух вокруг сгустился, будто сама тьма'
                ' решила взглянуть тебе в глаза. Из сумрака старой рощи, что тянется вдоль тракта, вышло чудовище.\n'
                ' \n'
                'Его тело — сплетение костей и гниющей плоти, вгрызшейся в доспехи павших. Из глазниц черепа струится'
                ' зеленоватый мрак, а когти — длинные, как кинжалы — скребут по земле, оставляя глубокие борозды.'
                ' Это — Падший Страж, слуга Лича, посланный, чтобы уничтожить любого, кто посмеет приблизиться к горе.\n'
                ' \n'
                'С рыком, от которого стынет кровь, он бросается на тебя, поднимая клубы пыли и тьмы.\n'
                ' Испытание началось. Приготовься к бою!\n'
            ),
            2: (
                'Глава 2. Город\n'
                ' \n'
                'Под мрачной тенью замка Лича раскинулся город — последний оплот перед неизбежной битвой. '
                'Здесь каждый шаг — шанс выжить, каждая встреча — возможность изменить судьбу. Но время'
                ' не на твоей стороне…\n'
                ' \n'
                'Куда направишься первым: в таверну, на рынок или в храм? \n'
            ),
            2.1: ('Ты заходишь в полутёмное помещение, пропахшее дымом, жареным мясом и дешёвым элем. '
                  'За стойкой — угрюмый трактирщик. В дальнем углу сидит старик с потухшим взглядом и потёртой эмблемой'
                  ' ордена на плаще. Он пьёт в одиночестве.\n'),
            2.12: (
                'Ты просишь поесть или переночевать без оплаты. Трактирщик хмурится и коротко кивает на дверь.\n'
                ' \n'
                'Трактирщик (резко):\n'
                '— Не благотворительность здесь, странник. Или плати, или проваливай.\n'
                '(пауза)\n'
                '— И даже не думай лезть к старому Мартену. Он не любит тех, кто приходит с пустыми руками.\n'
                ' \n'
                'После этого вы выходите из таверны, куда направится теперь?\n'
            ),
            2.11: (
                'Ты кладёшь на стойку 5 золотых. Трактирщик кивает, молча подаёт еду и ключ от комнаты. Через некоторое'
                ' время он немного теплеет.\n'
                ' \n'
                'Трактирщик (сдержанно, но с уважением):\n'
                '— Ты не похож на тех, кто просто ищет тёплую постель. Замок Лича не даёт покоя, да?\n'
                '(пауза)\n'
                '— Видишь вон того в углу? Это Сер Мартен. Когда-то он был паладином Света. Один из немногих,'
                ' кто вернулся с той бойни… Если поставишь ему выпить, может, и заговорит.\n'
            ),
            2.111: (
                'Ты подходишь к старику и ставишь перед ним кружку тёмного эля. Он медленно поднимает глаза, в которых'
                ' вспыхивает слабый отблеск прошлого величия.\n'
                ' \n'
                'Сэр Мартен (хрипло):\n'
                '— Эх… давно никто не делал мне таких подарков. Спасибо, путник.\n'
                '— Думаешь идти в замок? Глупец… или герой.\n'
                '(пауза)\n'
                '— Хочешь знать, что ждёт тебя за этими стенами? Слушай, пока я ещё помню.\n'
                ' \n'
                '(пауза, он смотрит в сторону)\n'
                '— Лич боится огня истины. Мы звали это так — заклинание, которое жрец наш'
                ' создал. Оно обжигало не плоть, а душу. Но нужно быть рядом. Очень рядом…\n'
                ' \n'
                'Получено заклинание: Огонь истины — заклинание, которое можно использовать один раз в бою'
                ' с Личом, чтобы снизить его защиту.\n'
                ' \n'
                'Сэр Мартен (в конце):\n'
                '— Я стар. Я сломался… Но ты — ты ещё можешь сделать то, что мы не смогли. Иди с открытыми глазами,'
                ' путник.\n'
                ' \n'
                'Вы прощаетесь с Сером Мартеном и выходите из таверны\n'
            ),
            2.112: "Вы уходите из таверны, так и не поговорив с Сером Мартеном\n",
            2.2: (
                'Ты выходишь на пыльную площадь.У лавок шумно, пахнет специями, металлом и волшебной пылью.Продавцы'
                ' зазывают редкими товарами, каждый утверждает, что именно его товар спасёт тебя от неминуемой гибели.\n'
                ' \n'
                'Ради уничтожение Лича торговцы готовы дать тебе снаряжение бесплатно, но рынок большой и чтобы не'
                ' терять слишком много времени, ты можешь пойти только к двум. Выбирай с умом.\n'
            ),
            2.21: 'Флакон рубинового цвета. Слегка тёплый. Пахнет чем-то древним и сильным.\n',
            2.22: 'Кузнец молча берёт твоё оружие, капает на него странное зелье и опускает в огонь синим пламенем.\n',
            2.23: 'Твоя броня покрывается рунной вязью. Она холодит кожу, но ты чувствуешь: она защитит.\n',
            2.24: 'Маг кладёт руку тебе на лоб. Ты ощущаешь, как древние слова проникают в разум.'
                  ' «Когда встретишься с тьмой — просто произнеси».\n',
            2.3: (
                'Ты входишь в храм — прохладный воздух обволакивает, несмотря на жар снаружи. Стены из чёрного камня,'
                ' алтарь украшен знаками света. Здесь тихо. Даже тишина как будто молится.\n'
                ' \n'
                'Жрица Света (спокойным голосом):\n'
                '— Не каждый ищет благословение. Но ты стоишь перед вратами холода и тьмы.\n'
                '— Замок Лича пропитан древним морозом. Его магия леденит кости и душу. Но Свет может защитить. \n'
            ),
            2.31: (
                'Ты склоняешься перед алтарём. Жрица возлагает ладони на твоё чело. Волна тепла проходит сквозь тело.'
                ' Лёд, что жил внутри тебя — исчезает.\n'
                ' \n'
                'Жрица (шёпотом):\n'
                '— Теперь он не сможет заморозить твой дух. Но остерегайся — Лич владеет не только льдом…\n'
                ' \n'
                'Теперь вы не уязвиму к холоду Лича и уходите из храма.\n'
            ),
            2.32: (
                'Жрица(тихо):\n'
                '— Значит, ты идёшь своим путём.Пусть свет всё же будет рядом, даже если ты отвернулся.\n'
                ' \n'
                'Ты понимаешь, что это может сыграть с тобой плохую шутку. Но выбор уже сделан и вы выходите из Храма.\n'
            ),
            2.5: (
                'Ты выходишь из города, благословённый светом и защищённый от холода.Вдохнув свежий воздух, ты'
                ' направляешься к замку Лича.Но едва ступив на дорогу, ты ощущаешь странное присутствие.\n'
                ' \n'
                'Что-то не так… Ощущение тревоги, как будто сама тьма следит за каждым твоим шагом. '
                'Ты оглядываешься — и вот он…\n'
                ' \n'
                'Темный рыцарь появляется из тени. Он высокий, в чёрной броне,'
                ' покрытой паутиной замороженных кровавых узоров.'
                ' Его глаза горят красным светом, и в руках он держит черный меч, пульсирующий зловещей энергией.\n'
                ' \n'
                'Тёмный рыцарь:\n'
                '— Ты думаешь, что избежал Лича, лишь потому что ты скрыт от его холода? Ты лишь приманка для него.\n'
                '(смеётся)\n'
                '— Этот путь не для тебя. Твой свет… угаснет в тени.\n'
                ' \n'
                ''
                'Ты должен сразиться с ним, чтобы продолжить путь. У него особая сила, но его могущество не безгранично.\n'
            ),
            3: (
                'Глава 3: Сердце тьмы\n'
                ' \n'
                'Врата замка распахнуты. Не скрипят, не скрежещут — просто распахнуты, будто ждали именно тебя.'
                ' Внутри — холод, тишина и дыхание смерти. Всё, что ты узнал, всё, что пережил… привело тебя сюда.\n'
                ' \n'
                'Ты входишь. Позади — город, тепло, жизнь. Впереди — Лич.\n'
                ' \n'
                'Ты идёшь по залам из чёрного камня. Под ногами — иней. Огни факелов не колышутся.'
                ' В каждом углу — шёпот. Но не живой. Это шепчет сама смерть.\n'
                ' \n'
                'В центре тронного зала сидит Лич — в позолоченной короне, его лицо — череп с глазами,'
                ' горящими синим пламенем. Его голос — как ветер из склепа:\n'
                ' \n'
                'Лич:\n'
                '— Я думал, ты будешь дольше умирать в пути.\n'
                '(пауза)\n'
                '— Ты хорошо подготовился… Но что ты сделаешь, когда я загляну в твою душу?\n'
                ' \n'
                'Время пришло. Используй всё, что у тебя есть. Судьба этого края зависит только от тебя.\n'
            )}

        self.dict_character_choices = {0: {1: "Да, я готов"},
                                       1: {1: "Атаковать мечом",
                                           2: "Атаковать арбалетом",
                                           3: "Атаковать огненым шаром"},
                                       1.1: {1: "Продолжить путь"},
                                       2: {1: "Отправиться в таверну",
                                           2: "Отправиться на рынок",
                                           3: "Отправиться в церковь"},
                                       2.1: {1: "Потратить 5 золотых",
                                             2: "Не платить"},
                                       2.11: {1: "Поставить выпивку Паладину (ещё -1 золото)",
                                              2: "Уйти"},
                                       2.12: {},
                                       2.111: {},
                                       2.112: {},
                                       2.2: {1: "Купить зелье жизни (+20% к общему здоровью)",
                                             2: "Улучшить оружие и посох (теперь вы наносите 3 урона",
                                             3: "Улучшить броню (теперь атаки врага на 2 урона меньше",
                                             4: "Изучить мощное заклинание против Лича (одноразовое заклинание"
                                                " большого урона)"},
                                       2.21: {},
                                       2.22: {},
                                       2.23: {},
                                       2.24: {},
                                       2.3: {1: "Попросить благословление (-5 монет)",
                                             2: "Попросить благословление (-5 HP)",
                                             3: "Отказаться"},
                                       2.31: {},
                                       2.32: {},
                                       2.4: {1: "Отправится к воротам"},
                                       2.5: {1: "Атаковать мечом",
                                             2: "Атаковать арбалетом",
                                             3: "Атаковать огненым шаром"},
                                       2.51: {1: "Продолжить путь"},
                                       3: {1: "Атаковать мечом",
                                           2: "Атаковать арбалетом",
                                           3: "Атаковать огненым шаром",
                                           4: "Использовать 'Огонь истины'",
                                           5: "Атаковать мощным заклинанием"}}

    def get_sessionStorage(self):
        return self.sessionStorage

    def set_sessionStorage(self, new_storage):
        self.sessionStorage = new_storage

    def get_dict_text_alice(self):
        return self.dict_text_alice

    def get_dict_character_choices(self):
        return self.dict_character_choices

    def get_completed_sections(self):
        return self.completed_sections

    def get_marten_spell(self):
        return self.marten_spell


app = Flask(__name__)

game = Game()


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    user_id = request.json['session']['user_id']

    if game.get_sessionStorage() == {}:
        introduction(request.json, response)
    elif game.get_sessionStorage()[user_id]['stade'] == 0:
        introduction(request.json, response)
    elif 1 <= game.get_sessionStorage()[user_id]['stade'] < 2:
        road_citi(request.json, response)
    elif 2 <= game.get_sessionStorage()[user_id]['stade'] < 3:
        citi(request.json, response)
    elif game.get_sessionStorage()[user_id]['stade'] == 3:
        battle_the_lich_king(request.json, response)

    logging.info(f'Response:  {response!r}')

    return jsonify(response)


def introduction(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        game.sessionStorage[user_id] = {
            'stade': 0,
            'hero': Hero(),
            'enemy': None
        }
        res['response']['text'] = writing_a_text(req)
        return
    if req['request']['original_utterance'] == '1':
        game.sessionStorage[user_id]['stade'] = 1
        game.sessionStorage[user_id]['enemy'] = The_Fallen_Guardian()
        res['response']['text'] = writing_a_text(req) + (f"HP у вас: {game.sessionStorage[user_id]['hero'].get_HP()}\n"
                                                         f"HP у противника: {game.sessionStorage[user_id]['enemy'].get_HP()}\n"
                                                         f"Дистанция до противника: {game.sessionStorage[user_id]['enemy'].get_distance()}")
    else:
        res['response']['text'] = "Скажите, когда будете готовы отправиться"


def road_citi(req, res):
    user_id = req['session']['user_id']
    if game.sessionStorage[user_id]['stade'] == 1:
        battle_the_fallen_guardian(req, res)
    elif game.sessionStorage[user_id]['stade'] == 1.1:
        if req['request']['original_utterance'] == '1':
            game.sessionStorage[user_id]['stade'] = 2
            res['response']['text'] = writing_a_text(req)
        else:
            res['response']['text'] = "Скажите, когда будете готовы отправиться"


def citi(req, res):
    user_id = req['session']['user_id']
    if game.sessionStorage[user_id]['stade'] == 2:
        if req['request']['original_utterance'] in ["1", "2", "3"]:
            number = int(req['request']['original_utterance'])
            if number == 1:
                if game.completed_tavern:
                    res['response']['text'] = ("Вы уже прошли эту зону, выберете другую\n" +
                                               actions(game.get_dict_character_choices()[
                                                           game.get_sessionStorage()[user_id]['stade']]))
                    return
                game.sessionStorage[user_id]['stade'] = 2.1
                res['response']['text'] = writing_a_text(
                    req) + f"Монет сейчас: {game.sessionStorage[user_id]['hero'].get_coin()}"
            elif number == 2:
                if game.completed_market:
                    res['response']['text'] = ("Вы уже прошли эту зону, выберете другую\n" +
                                               actions(game.get_dict_character_choices()[
                                                           game.get_sessionStorage()[user_id]['stade']]))
                    return
                game.sessionStorage[user_id]['stade'] = 2.2
                res['response']['text'] = writing_a_text(req)
            elif number == 3:
                if game.completed_church:
                    res['response']['text'] = ("Вы уже прошли эту зону, выберете другую\n" +
                                               actions(game.get_dict_character_choices()[
                                                           game.get_sessionStorage()[user_id]['stade']]))
                    return
                game.sessionStorage[user_id]['stade'] = 2.3
                res['response']['text'] = writing_a_text(req)
        else:
            res['response']['text'] = "Скажите, куда отправится"
    elif 2.1 <= game.sessionStorage[user_id]['stade'] < 2.2:
        tavern(req, res)
    elif 2.2 <= game.sessionStorage[user_id]['stade'] < 2.3:
        market(req, res)
    elif 2.3 <= game.sessionStorage[user_id]['stade'] < 2.4:
        church(req, res)
    elif game.sessionStorage[user_id]['stade'] == 2.4:
        if req['request']['original_utterance'] == '1':
            game.sessionStorage[user_id]['stade'] = 2.5
            game.sessionStorage[user_id]['enemy'] = The_Dark_Knight()
            res['response']['text'] = writing_a_text(req) + (
                f"HP у вас: {game.sessionStorage[user_id]['hero'].get_HP()}\n"
                f"HP у противника: {game.sessionStorage[user_id]['enemy'].get_HP()}\n"
                f"Дистанция до противника: {game.sessionStorage[user_id]['enemy'].get_distance()}")
        else:
            res['response']['text'] = "Скажите, когда будете готовы отправиться"
    elif game.sessionStorage[user_id]['stade'] == 2.5:
        battle_the_dark_knight(req, res)
    elif game.sessionStorage[user_id]['stade'] == 2.51:
        if req['request']['original_utterance'] == '1':
            game.sessionStorage[user_id]['stade'] = 3
            game.sessionStorage[user_id]['enemy'] = The_Lich_King()
            res['response']['text'] = writing_a_text(req) + (
                f"HP у вас: {game.sessionStorage[user_id]['hero'].get_HP()}\n"
                f"HP у противника: {game.sessionStorage[user_id]['enemy'].get_HP()}\n"
                f"Дистанция до противника: {game.sessionStorage[user_id]['enemy'].get_distance()}")
        else:
            res['response']['text'] = "Скажите, когда будете готовы отправиться"


def church(req, res):
    user_id = req['session']['user_id']
    if req['request']['original_utterance'] in ["1", "2", "3"]:
        number = int(req['request']['original_utterance'])
        if number == 1:
            if game.sessionStorage[user_id]['hero'].get_coin() < 5:
                res['response']['text'] = "У вас не хватает денег на благословление\n" + actions(
                    game.get_dict_character_choices()[2.3])
                return
            game.sessionStorage[user_id]['hero'].set_coin(game.sessionStorage[user_id]['hero'].get_coin() - 5)
            game.sessionStorage[user_id]['hero'].set_vulnerability_to_cold(False)
            game.sessionStorage[user_id]['stade'] = 2.31
        elif number == 2:
            game.sessionStorage[user_id]['hero'].set_HP(game.sessionStorage[user_id]['hero'].get_HP() - 5)
            game.sessionStorage[user_id]['hero'].set_vulnerability_to_cold(False)
            game.sessionStorage[user_id]['stade'] = 2.31
        elif number == 3:
            game.sessionStorage[user_id]['stade'] = 2.32
        if game.get_completed_sections() == 2:
            res['response']['text'] = writing_a_text(
                req) + ('Ты посетил все зоны в городе, пора отправлятся к'
                        ' городским воротам\n') + actions(game.get_dict_character_choices()[2.4])
            game.sessionStorage[user_id]['stade'] = 2.4
            return
        res['response']['text'] = (writing_a_text(
            req) + actions(game.get_dict_character_choices()[2]))
        game.completed_sections += 1
        game.completed_church = True
        game.sessionStorage[user_id]['stade'] = 2
    else:
        res['response']['text'] = "Выберите вариант ответа"


def market(req, res):
    user_id = req['session']['user_id']
    if req['request']['original_utterance'] in ["1", "2", "3", "4"]:
        number = int(req['request']['original_utterance'])
        if game.purchased_items[number]:
            res['response']['text'] = "Вы уже купили этот предмет. Выберете другой\n" + actions(
                game.get_dict_character_choices()[game.get_sessionStorage()[user_id][2.2]])
            return
        game.purchased_items[number] = True
        if number == 1:
            game.sessionStorage[user_id]['hero'].set_HP(game.sessionStorage[user_id]['hero'].get_HP() + 5)
            game.sessionStorage[user_id]['hero'].set_max_HP(game.sessionStorage[user_id]['hero'].get_HP())
            game.sessionStorage[user_id]['stade'] = 2.21
        elif number == 2:
            game.sessionStorage[user_id]['hero'].set_AP(game.sessionStorage[user_id]['hero'].get_AP() + 1)
            game.sessionStorage[user_id]['stade'] = 2.22
        elif number == 3:
            game.sessionStorage[user_id]['hero'].set_protection(
                game.sessionStorage[user_id]['hero'].get_protection() + 2)
            game.sessionStorage[user_id]['stade'] = 2.23
        elif number == 4:
            game.powerful_spell = True
            game.sessionStorage[user_id]['stade'] = 2.24
        game.equipment_is_taken += 1
        if game.equipment_is_taken == 2:
            if game.get_completed_sections() == 2:
                res['response']['text'] = writing_a_text(
                    req) + "Ты взял вещи которые посчитал нужными, больше задерживатся здесь нельзя\n" + (
                                              'Ты посетил все зоны в городе, пора отправлятся к'
                                              ' городским воротам\n') + actions(game.get_dict_character_choices()[2.4])
                game.sessionStorage[user_id]['stade'] = 2.4
                return
            res['response']['text'] = (writing_a_text(
                req) + "Ты взял вещи которые посчитал нужными, больше задерживатся здесь нельзя\n" +
                                       actions(game.get_dict_character_choices()[2]))
            game.completed_sections += 1
            game.completed_market = True
            game.sessionStorage[user_id]['stade'] = 2
            return
        res['response']['text'] = writing_a_text(req) + actions(game.get_dict_character_choices()[2.2])
    else:
        res['response']['text'] = "Выберите товар"


def tavern(req, res):
    user_id = req['session']['user_id']
    if game.sessionStorage[user_id]['stade'] == 2.1:
        if req['request']['original_utterance'] in ["1", "2"]:
            if int(req['request']['original_utterance']) == 1:
                game.sessionStorage[user_id]['hero'].set_coin(game.sessionStorage[user_id]['hero'].get_coin() - 5)
                game.sessionStorage[user_id]['stade'] = 2.11
                if game.sessionStorage[user_id]['hero'].get_coin() < 1:
                    game.not_coin_for_marten_spell = True
                    res['response']['text'] = writing_a_text(req) + (
                        "И вдруг вы понимаете, у вас не осталось денег на ещё"
                        "одну выпивку.")
                else:
                    res['response']['text'] = writing_a_text(req)
            else:
                game.sessionStorage[user_id]['stade'] = 2.12
                if game.get_completed_sections() == 2:
                    res['response']['text'] = writing_a_text(req) + ('Ты посетил все зоны в городе, пора отправлятся к'
                                                                     ' городским воротам\n') + actions(
                        game.get_dict_character_choices()[2.4])
                    game.sessionStorage[user_id]['stade'] = 2.4
                else:
                    game.completed_tavern = True
                    res['response']['text'] = writing_a_text(req) + actions(game.get_dict_character_choices()[2])
                    game.completed_sections += 1
                    game.sessionStorage[user_id]['stade'] = 2
        else:
            res['response']['text'] = "Выберите вариант ответа"
    elif game.sessionStorage[user_id]['stade'] == 2.11:
        if req['request']['original_utterance'] in ["1", "2"]:
            if int(req['request']['original_utterance']) == 1:
                if game.not_coin_for_marten_spell:
                    res['response']['text'] = "У вас нет денег на это\n" + actions(
                        game.get_dict_character_choices()[2.11])
                    return
                game.sessionStorage[user_id]['hero'].set_coin(game.sessionStorage[user_id]['hero'].get_coin() - 1)
                game.sessionStorage[user_id]['stade'] = 2.111
                if game.get_completed_sections() == 2:
                    res['response']['text'] = writing_a_text(req) + ('Ты посетил все зоны в городе, пора отправлятся к'
                                                                     ' городским воротам\n') + actions(
                        game.get_dict_character_choices()[2.4])
                    game.sessionStorage[user_id]['stade'] = 2.4
                else:
                    game.completed_tavern = True
                    game.not_marten_spell = True
                    res['response']['text'] = writing_a_text(req) + actions(game.get_dict_character_choices()[2])
                    game.completed_sections += 1
                    game.sessionStorage[user_id]['stade'] = 2
            else:
                game.sessionStorage[user_id]['stade'] = 2.112
                if game.get_completed_sections() == 2:
                    res['response']['text'] = writing_a_text(req) + ('Ты посетил все зоны в городе, пора отправлятся к'
                                                                     ' городским воротам\n') + actions(
                        game.get_dict_character_choices()[2.4])
                    game.sessionStorage[user_id]['stade'] = 2.4
                else:
                    game.completed_tavern = True
                    res['response']['text'] = writing_a_text(req) + actions(game.get_dict_character_choices()[2])
                    game.completed_sections += 1
                    game.sessionStorage[user_id]['stade'] = 2
        else:
            res['response']['text'] = "Выберите вариант ответа"
    else:
        res['response']['text'] = "Выберите вариант ответа"


def writing_a_text(req):
    user_id = req['session']['user_id']
    stade = game.get_sessionStorage()[user_id]['stade']
    return game.get_dict_text_alice()[stade] + actions(game.get_dict_character_choices()[stade])


def actions(dict_actions):
    string_actions = ''
    for i in range(1, len(dict_actions) + 1):
        string_actions += f'{i}: {dict_actions.get(i)}\n'
    if string_actions is None:
        string_actions = ' '
    return string_actions


def battle_the_fallen_guardian(req, res):
    user_id = req['session']['user_id']
    attack = req['request']['original_utterance']
    if attack in ['1', '2', '3']:
        result_battle = game.sessionStorage[user_id]['enemy'].battle(int(attack), game.sessionStorage[user_id]['hero'])
        if game.sessionStorage[user_id]['hero'].get_dead():
            res['response']['text'] = result_battle
            res['response']['end_session'] = True
            return
        if game.sessionStorage[user_id]['enemy'].get_Dead():
            game.sessionStorage[user_id]['enemy'] = None
            game.sessionStorage[user_id]['stade'] = 1.1
            res['response']['text'] = result_battle + actions(
                game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
        else:
            res['response']['text'] = result_battle + actions(
                game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
    else:
        res['response']['text'] = "Скажите, чем будете атаковать!"


def battle_the_dark_knight(req, res):
    user_id = req['session']['user_id']
    attack = req['request']['original_utterance']
    if attack in ['1', '2', '3']:
        result_battle = game.sessionStorage[user_id]['enemy'].battle(int(attack), game.sessionStorage[user_id]['hero'])
        if game.sessionStorage[user_id]['hero'].get_dead():
            res['response']['text'] = result_battle
            res['response']['end_session'] = True
            return
        if game.sessionStorage[user_id]['enemy'].get_Dead():
            game.sessionStorage[user_id]['enemy'] = None
            game.sessionStorage[user_id]['stade'] = 2.51
            res['response']['text'] = result_battle + actions(
                game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
        else:
            res['response']['text'] = result_battle + actions(
                game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])


def battle_the_lich_king(req, res):
    user_id = req['session']['user_id']
    attack = req['request']['original_utterance']
    if attack in ['1', '2', '3', '4', '5']:
        if attack == '4':
            if game.marten_spell is False:
                res['response']['text'] = "Вы не поговрили с Мартеном и не можете использовать 'Огонь веры'" + actions(
                    game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
                return
        if attack == '5':
            if game.powerful_spell is False:
                res['response']['text'] = "Вы не купили мощьное заклинание и не можете его использовать" + actions(
                    game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
                return
        result_battle = game.sessionStorage[user_id]['enemy'].battle(int(attack), game.sessionStorage[user_id]['hero'])
        if game.sessionStorage[user_id]['hero'].get_dead():
            res['response']['text'] = result_battle
            res['response']['end_session'] = True
            return
        if game.sessionStorage[user_id]['enemy'].get_Dead():
            if game.sessionStorage[user_id]['enemy'].self.marten_spell is True and game.sessionStorage[user_id][
                'hero'].self.vulnerability_to_cold is False:
                res['response']['text'] = (
                    'Ты наносишь последний удар. Лич рушится, его тело исчезает в вихре инея и праха. Корона падает к'
                    ' твоим ногам. Вокруг — мрак и молчание. Ты остался один.\n'

                    '— Трон пуст. Корона зовёт. Её магия проникает в твои мысли.\n'
                    '— Надень её...\n'
                    '— Стань вечным.\n'
                    'Ты поднимаешь корону… но ощущаешь, как она дрожит в твоих руках. Заклятие Сэра Мартена вспыхивает'
                    ' в памяти, как щит, а свет храма — греет душу изнутри. Корона больше не властна над тобой.\n'
                    'Ты бросаешь корону в ледяную бездну.Слышится отдалённый визг, будто сама тьма теряет силу.Ты покидаешь тронный зал — человеком.'

                    '→ Конец.“Ты победил… и остался собой.”'
                )
        else:
            res['response']['text'] = result_battle + actions(
                game.get_dict_character_choices()[game.sessionStorage[user_id]['stade']])
    else:
        res['response']['text'] = "Скажите, чем будете атаковать!"


if __name__ == '__main__':
    app.run()
