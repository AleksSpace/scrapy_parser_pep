# Парсер информации о PEP
## Стек
```
Python 3.9.13
Scrapy
```
Парсер собирает информацию со страницы https://peps.python.org/

После сбора информации парсер сохраняет всю собранную информацию в два файла .scv
В один файл сохраняются данные о PEP - «Номер», «Название» и «Статус».
В другой файл сохраняются данные о PEP - «Статус» и «Количество».

## Запуск проекта
Для запуска вам нужно:
1) Клонировать репозиторий себе на компьютер при помощи одной из команд:
```
git clone https://github.com/AleksSpace/scrapy_parser_pep.git
git clone git@github.com:AleksSpace/scrapy_parser_pep.git
git clone gh repo clone AleksSpace/scrapy_parser_pep
```
2) Перейти в репозиторий, установить виртуальное окружение и активировать его:
```
python -m venv venv
. venv/Scripts/activate
```
3) Обновить pip и установить зависимости
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
4) запустите паука при помощи команды:
```
scrapy crawl pep
```

### Автор
- [Заикин Алексей](https://github.com/AleksSpace "GitHub аккаунт")
