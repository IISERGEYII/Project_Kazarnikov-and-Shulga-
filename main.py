import logging
from flask import Flask, request, jsonify
from Logic.Logic_game import Warrior, Archer, Mag, Enemy, Armor, Weapon, Regen

app = Flask(__name__)
sessionStorage = {}


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

    if sessionStorage.get(user_id) is None:
        create_hero(request.json, response)
    else:
        stade = sessionStorage[user_id]['stade']
        if stade == 1:
            create_hero(request.json, response)
        elif srade == 2:
            road_citi(request.json, response)
        elif stade == 3:
            citi(request.json, response)
        else:
            main_enemy(request.json, response)

    logging.info(f'Response:  {response!r}')

    return jsonify(response)


def create_hero(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        sessionStorage[user_id] = {
            'stade': 1,
            'class': None
        }
        res['response']['text'] = ('Здравсвуй! Для начала введу тебя в курс дела. Тебя выбрали для того чтобы'
                                   'уничтожить лича, что недавно пробудился от сна в городе неподалёку.'
                                   ''
                                   ' Напомни, кто твой класс?')
        return

    if sessionStorage[user_id]['class'] is None:
        clas = req['request']['original_utterance'].lower()
        if clas == 'воин':
            sessionStorage[user_id]['class'] = Warrior()
            res['response']['text'] = ("Значит воин. Надеюсь меч и секира тебя не подведут."
                                       ""
                                       " Оружие в первом слоте: Меч"
                                       "Оружие во втором слоте: Секира")
            print(sessionStorage[user_id]['class'])
        elif clas == 'лучник':
            sessionStorage[user_id]['class'] = Archer()
            res['response']['text'] = ("Лучник. Иногда лучше осыпать врага градом стрел, чем идти в ближний бой"
                                       ""
                                       "Оружие в первом слоте: Лук"
                                       "Оружие во втором слоте: Короткий меч")
            print(sessionStorage[user_id]['class'])
        elif clas == 'маг':
            sessionStorage[user_id]['class'] = Mag()
            res['response']['text'] = ("Маг. Ты же выучил свои заклинания, верно?"
                                       ""
                                       "Оружие в первом слоте: Огненый шар"
                                       "Оружие во втором слоте: Кинжал")
            print(sessionStorage[user_id]['class'])
        else:
            res['response']['text'] = "Нераслышал, повтори"


def road_citi(req, res):
    pass


def citi(req, res):
    pass


def main_enemy(req, res):
    pass


if __name__ == '__main__':
    app.run()
