# Phone Authorization Service API

API для функционала авторизации через номера телефона.

## Эндпоинты (Endpoints)

### Аутентификация пользователя

URL: /auth/

Метод: POST

Описание: Проверяет наличие пользователя в базе данных и возвращает одноразовый код для подтверждения авторизации.

Параметры запроса:
- phone_number (обязательный) - номер телефона пользователя.

Пример запроса:

{
    "phone_number": "89123456789"
}

Ответ:

{
    "otp_code": "1234"
}

### Обновление кода аутентификации

URL: /auth/

Метод: POST

Описание: Проверяет подтверждающий код аутентификации пользователя и возвращает access token для доступа к другим эндпоинтам API.

Параметры запроса:
- phone_number (обязательный) - номер телефона пользователя.
- otp_code (обязательный) - проверочный код, полученный после аутентификации.

Пример запроса:

{
    "phone_number": "89123456789",
    "otp_code": "1234"
}

Ответ:

{
    "access_token": "..."
}

### Получение профиля пользователя

URL: /profile/

Метод: GET

Описание: Возвращает информацию о профиле пользователя, включая его номер телефона и другую информацию.

Пример ответа:

{
    "phone_number": "89123456789",
    "invite_code": "ABCD123",
    "other_profile_invite_code": "EFGH456",
    "invited_users": [
        "89543210987",
        "89765432109"
    ]
}

### Активация чужого инвайт кода

URL: /profile/

Метод: POST

Описание: Позволяет пользователю активировать чужой инвайт код в своем профиле.

Параметры запроса:
- other_profile_invite_code (обязательный) - чужой инвайт код.

Пример запроса:

{
    "other_profile_invite_code": "EFGH456"
}

Ответ:

{
    "message": "Чужой инвайт код был успешно активирован в профиле пользователя."
}

## Запуск проекта
1. Создайте в корне проекта файл ```.env``` и заполните данные по образцу из файла ```.env.sample```

2. Создайте виртуальное окружение ``venv```
   ```shell
   python3 -m venv venv
   ```

3. Установите все необходимые зависимости, указанные в файле ```requirements.txt```
   ```shell
   pip install -r requirements.txt
   ```

4. Произведите миграции базы данных командами
   ```shell
      python3 manage.py makemigration
      ```
   ```shell
      python3 manage.py migrate
      ```
   
5. Для работы с админкой необходимо создать суперпользователя командой:
   ```shell
   python3 manage.py csu
   ```

6. Запустите сервер командой
   ```shell
   python3 manage.py runserver
   ```


## Запуск проекта с Docker

1. Создать Docker контейнер командой:
```shell
docker-compose build
```
2. Запустить Docker контейнер командой:
```shell
docker-compose up
```
После выполнения команд произойдёт:
- создание контейнера, загрузка и собор всех необходимых образов
- создание базы данных и выполнение всех необходимых миграций
- запуск сервера на порту ```0.0.0.0:8000```