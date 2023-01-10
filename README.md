![](https://img.shields.io/badge/Python-3.7.0-blue?style=flat&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-3.2.15-orange?style=flat&logo=django&logoColor=white)

# Web-приложение для определения заполненных форм.
******
Данное приложение было выполнено в рамках тестового задания

[Тестовое задание на вакансию разработчик Python](https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit)
******
## ⚙ Используемые технологии: 
▪ **Python**<br> 
▪ **Django**<br>

## Запуск web-приложения

~~~docker
docker-compose build --no-cache
docker-compose up -d
~~~
Для проверки работоспособности запустить script_requests.py   

Если возникает ошибка permission denied": unknown при docker-compose up -d
нужно использовать команду chmod +x ./entrypoint.sh
и после пересобрать контейнер сначала.