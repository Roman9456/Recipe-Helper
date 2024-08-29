# Recipe Helper

The Recipe Helper is a simple web service that provides a list of ingredients and their quantities for preparing various dishes.

## Features

- The service knows a set of recipes (see the calculator/views.py file - the DATA variable).
- Requesting a URL like /omlet/ will return the list of ingredients and their quantities for making an omelet.
- Requesting a URL like /pasta/ will return the list of ingredients and their quantities for making macaroni and cheese.
- The service provides the ingredient quantities for a single portion by default.
- If the optional servings parameter is provided (a positive integer), the service will return the ingredient quantities for the specified number of portions.

## Usage

1. Install the dependencies:

   pip install -r requirements.txt

2. Start the server:

   python manage.py runserver

3. Access the service using the following URLs:
   - /omlet/: Get the ingredients and quantities for an omelet.
   - /pasta/: Get the ingredients and quantities for macaroni and cheese.
   - /omlet/?servings=4: Get the ingredients and quantities for 4 portions of an omelet.

## Implementation Details

- The servings parameter is optional, so it may not be present in the requests.GET data.
- The parameters from requests.GET are always strings, so they need to be converted to numbers for multiplication.
- The context should look similar to this:

  context = {
    'recipe': {
      'ingredient1': quantity1,
      'ingredient2': quantity2,
    }
  }

  # Помощник по Рецептам

Помощник по Рецептам - это простой веб-сервис, который предоставляет список ингредиентов и их количества для приготовления различных блюд.

## Возможности

- Сервис знает некоторое количество рецептов (см. файл calculator/views.py - переменная DATA).
- Запрос URL вида /omlet/ вернет список ингредиентов и их количества для приготовления омлета.
- Запрос URL вида /pasta/ вернет список ингредиентов и их количества для приготовления макарон с сыром.
- Сервис предоставляет количество ингредиентов на одну порцию по умолчанию.
- Если передать необязательный параметр servings (положительное целое число), сервис вернет количество ингредиентов на указанное число порций.

## Использование

1. Установите зависимости:

   pip install -r requirements.txt

2. Запустите сервер:

   python manage.py runserver

3. Получите доступ к сервису, используя следующие URL-адреса:
   - /omlet/: Получите ингредиенты и количество для омлета.
   - /pasta/: Получите ингредиенты и количество для макарон с сыром.
   - /omlet/?servings=4: Получите ингредиенты и количество для 4 порций омлета.

## Детали реализации

- Параметр servings является необязательным, поэтому он может отсутствовать в данных requests.GET.
- Параметры из requests.GET всегда являются строками, поэтому их необходимо преобразовывать в числа для умножения.
- Контекст должен выглядеть примерно следующим образом:

  context = {
    'recipe': {
      'ingredient1': quantity1,
      'ingredient2': quantity2,
    }
  }
