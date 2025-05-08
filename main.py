from flask import Flask, request, jsonify
from Logic import Logic_game
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

sessionStorage = {'class_offer': False}


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
        offer_class(request.json, response)

        logging.info(f'Response:  {response!r}')

        return jsonify(response)

def offer_class(req, res):
        user_id = req['session']['user_id']
        if req['session']['new']:
            res['response']['text'] = \
                'Здравствуй! Для начала введём тебя в курс дела. Тебя выбрали ради того чтобы уничтожить ' \
                + 'короля Лича, который своим пробуждением угрожает городу не по далёку' \
                + '' \
                + 'Сначала скажи, как тебя звать'
            sessionStorage[user_id] = {
                'first_name': None
            }
            return

        if sessionStorage[user_id]['first_name'] is None:
            # в последнем его сообщение ищем имя.
            first_name = get_first_name(req)
            # если не нашли, то сообщаем пользователю что не расслышали.
            if first_name is None:
                res['response']['text'] = \
                    'Не расслышала имя. Повтори, пожалуйста!'

def get_first_name(req):
        for entity in req['request']['nlu']['entities']:
            # находим сущность с типом 'YANDEX.FIO'
            if entity['type'] == 'YANDEX.FIO':
                # Если есть сущность с ключом 'first_name',
                # то возвращаем ее значение.
                # Во всех остальных случаях возвращаем None.
                return entity['value'].get('first_name', None)

if __name__ == '__main__':
    app.run()
