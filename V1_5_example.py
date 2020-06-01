import requests
import json

'''
Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:

Путь к файлу с текстом;
Путь к файлу с результатом;
Язык с которого перевести;
Язык на который перевести (по-умолчанию русский).
'''

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'AQVN08OIYdMF8D5rGIFOH-Xm5FnJYEd07nKIPjJP'
FOLDER_ID = 'ajejoe463ko5u0v6m641'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang): #initial_file_name, result_file_name, from_lang

    params = {
    'key': API_KEY,
    'texts': ['Переводи давай'],
    'format': 'plain',
    'lang': 'ru-en'
    }

    response = requests.post(URL, params=params)
    print(response)
    json_ = response.json()
    print(response.json())
    # return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    print(translate_it('А ну-ка переведи мне текст! Быстро!', 'en'))