# Telegram Currency Converter Bot

Этот проект представляет собой Telegram-бота для конвертации валют. Бот использует актуальные курсы валют и позволяет пользователям конвертировать суммы между различными валютами.

## Структура:

- config.py для хранения токена Telegram-бота.
- bot.py для основного кода бота.
- extensions.py для классов и методов обработки данных.


## Используемые библиотеки:

- pytelegrambotapi для взаимодействия с Telegram.
- requests для отправки HTTP-запросов к API валют.
- json для парсинга ответов API.

## Описание функционала:

- Пользователь может отправить запрос в формате <имя валюты> <имя валюты> <количество>, и бот вернет цену.
- Конвертация между валютами (USD, EUR, RUB)
- Получение актуальных курсов валют через API
- Обработка пользовательских ошибок
- Команды /start и /help будут предоставлять инструкции по использованию бота.
- Команда /values будет выводить список доступных валют.

## Переход в бота
[@NBa_QAP_Convert_Currency_bot](https://t.me/NBa_QAP_Convert_Currency_bot)
