import requests


HOST_URL = 'http://localhost:8000'
FIELDS_FOR_FIND = [{'new_email': 'test1@bk.ru',
                    'email': 'email@bk.ru'},

                   {'new_email': 'test1@bk.ru',
                    'email': 'email@bk.ru',
                    'first_name': 'Dmitriy', },
                   {'new_email': 'test1@bk.ru',
                    'email': 'email@bk.ru',
                    'first_name': 'Dmitriy',
                    'date': '28.05.1998'},
                   {},
                   {'empty': 'Sometimes not empty',
                    'lazy_day': '2023-01-06'}
                   ]


def get_form(field_for_find):
    print(field_for_find)
    response1 = requests.post(f'{HOST_URL}/get_form', data=field_for_find)
    print(response1.content.decode('utf-8'))


if __name__ == '__main__':
    response = requests.get(HOST_URL)

    if response.status_code == 200:

        print('Список шаблонов в базе данных',
              response.content.decode('utf-8').replace('</br>', '\n'),
              'Сервер успешно открыт, отправляем POST запрос',
              sep='\n')

        for n in range(len(FIELDS_FOR_FIND)):
            print(f'\n№{n+1}')
            get_form(FIELDS_FOR_FIND[n])
    else:
        print('Сервер отключен')
