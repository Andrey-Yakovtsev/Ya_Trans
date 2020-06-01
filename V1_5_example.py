import requests
from pprint import pprint
import os
import json
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

def translate_it(inputfile, outputfile, to_lang:'ru'):
    API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    with open(inputfile, encoding='utf-8') as initial_file:
        news = initial_file.read()

        params = {
            'key': API_KEY,
            'text': news,
            'lang': 'ru',
            'options': 1
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        pprint(json_['lang'])
        line = ''.join(json_['text'])

    with open (outputfile, 'w') as file_output:
        file_output.write(line)


def send_it_to_disk(filename):

    DISKURL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'OAuth AgAAAAA7LlbAAADLW2uUXegQwkg8qje0HgTqcEo'
    }

    params = {
        'path': os.path.join(filename),
        'overwrite': 'True'
    }

    response = requests.get(DISKURL, headers=headers, params=params)
    upload_url = response.json()['href']
    files = {'file': open(filename, 'rb')}
    upload_response = requests.put(upload_url, files=files)
    print(upload_response.status_code)
    files['file'].close()

translate_it('DE.txt', 'DE-RU.txt', 'ru')
send_it_to_disk('DE-RU.txt')

translate_it('FR.txt', 'FR-RU.txt', 'ru')
send_it_to_disk('FR-RU.txt')

translate_it('ES.txt', 'ES-RU.txt', 'ru')
send_it_to_disk('ES-RU.txt')

