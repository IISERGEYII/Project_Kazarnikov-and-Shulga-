from itertools import count

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
buy_elophant = False
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

    stade = sessionStorage.get('stade')
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


def handle_dialog(req, res):
    global buy_elophant
    user_id = req['session']['user_id']

    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': [
                "Не хочу.",
                "Не буду.",
                "Отстань!",
            ]
        }
        res['response']['text'] = 'Привет! Купи слона!'
        res['response']['buttons'] = get_suggests(user_id)
        return
    if buy_elophant:
        if req['request']['original_utterance'].lower() in [
            'ладно',
            'куплю',
            'покупаю',
            'хорошо',
            'я покупаю',
            'я куплю'
        ]:
            res['response']['text'] = 'Кролика можно найти на Яндекс.Маркете!'
            res['response']['end_session'] = True
            return

        res['response']['text'] = \
            f"Все говорят '{req['request']['original_utterance']}', а ты купи кролика!"
        res['response']['buttons'] = get_suggests(user_id)
    else:
        if req['request']['original_utterance'].lower() in [
            'ладно',
            'куплю',
            'покупаю',
            'хорошо',
            'я покупаю',
            'я куплю'
        ]:
            res['response']['text'] = 'Слона можно найти на Яндекс.Маркете! А теперь купи кролика!'
            buy_elophant = True
            return

        res['response']['text'] = \
            f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
        res['response']['buttons'] = get_suggests(user_id)


def create_hero(req, res):
    user_id = req['session']['user_id']


def road_citi(req, res):
    pass


def citi(req, res):
    pass


def main_enemy(req, res):
    pass


stade = {1: create_hero,
         2: road_citi,
         3: citi,
         4: main_enemy}


def get_suggests(user_id):
    session = sessionStorage[user_id]

    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

    return suggests


if __name__ == '__main__':
    app.run()
