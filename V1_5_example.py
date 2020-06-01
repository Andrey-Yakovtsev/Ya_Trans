import requests
from pprint import pprint
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



def translate_it(inputfile, outputfile, to_lang:'ru'):
    with open(inputfile, encoding='utf-8') as initial_file:
        news = initial_file.read()

        params = {
            'key': API_KEY,
            'text': news,
            'lang': 'ru',  #"'ru-{}'.format(to_lang)
            'options': 1
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        pprint(json_['lang'])
        line = ''.join(json_['text'])

    with open (outputfile, 'w') as file_output:
        file_output.write(line)


translate_it('DE.txt', 'DE-RU.txt', 'ru')
translate_it('ES.txt', 'ES-RU.txt', 'ru')
translate_it('FR.txt', 'FR-RU.txt', 'ru')


'''
Исходная версия


def translate_it(text, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': line,
        'lang': 'ru',  #"'ru-{}'.format(to_lang)
        'options': 1
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    pprint(json_['lang'])
    return ''.join(json_['text'])




if __name__ == '__main__':
    with open('DE.txt', encoding='utf-8') as initial_file:
        line = initial_file.read()
    with open ('DE-RU.txt', 'w') as file_output:
        file_output.write(translate_it('line', 'ru'))

'''