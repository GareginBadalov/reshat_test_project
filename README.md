# Реализована API интеграция приложения Django и платежной системы Stripe.

## Описание API

### Реализованы следующие методы:

* `admin/`

 -endpoint для админ панели Django, модели зарегестрированы, есть возможность добавлять, удалять изменять данные.

* `item/{itemId}`

 -endpoint для основной функции оплаты, в представлении происходит подстановка параметров объекта из модели в функию поиска объекта Product в Stripe для дальнейшего получения priceId, создается сессия Stripe происходит редирект на страницу оплаты.
* `order/{orderId}`

 -Аналогично предыдущему методу, только для набора items добавленных в order
* `buy/{itemId}`

-endpoint для получения Stripe sessionId, после получения происходит редирект на страницу оплаты
* `buy/order/{orderId}`

-Аналогично предыдущему методу, только для набора items
* `success/`

 -Страница успешного выполнения платежа
* `cancelled/`

 -Страница неуспешного выполнения платежа
* `itemList/`

-endpoint для получения списка всех объектов Items
* `item/create`

-endpoint для создания Item, В представлении реализовано создание объекта Product в Stripe, чтобы было соответствие данных в бд и Stripe
* `itemDetail/{itemId}/` 

-endpoint для детального представления Item

## Руководство по запуску проекта

### Локально, средствами Django

1. Клонировать репозиторий

    `https://github.com/GareginBadalov/reshat_test_project.git`
2. Создать локальное окружение
3. Установить зависимости

    `pip install -r requirements`
4. Установить переменные окружения
   1. PowerShell
   
   `$Env:STRIPE_PUBLISHABLE_KEY = pk_test_51LhZkNG0PTn54pjymDT2YwXpfa1k6aT6yoaaFj8MOFiMszXatmBGYVP6twQIcCeyI5pTBWBHX0DpUxnHMQL6IFbL00KTnQGXLI`
   
   `$Env:STRIPE_SECRET_KEY = sk_test_51LhZkNG0PTn54pjymvq4hfLemxyBK77RJz0Lkhso1A1Gp0mykLfi0QTqQxs1r7R1LoLRxrelrHScs8hBmuF2n21700q7XzaPqP`
   2. CMD
   
   `SET STRIPE_PUBLISHABLE_KEY=pk_test_51LhZkNG0PTn54pjymDT2YwXpfa1k6aT6yoaaFj8MOFiMszXatmBGYVP6twQIcCeyI5pTBWBHX0DpUxnHMQL6IFbL00KTnQGXLI`
   
   `SET STRIPE_SECRET_KEY=sk_test_51LhZkNG0PTn54pjymvq4hfLemxyBK77RJz0Lkhso1A1Gp0mykLfi0QTqQxs1r7R1LoLRxrelrHScs8hBmuF2n21700q7XzaPqP`
   3. Либо средствами IDE
5. Запустить Тестовый сервер Django

    `python manage.py runservr`
6. Перейти по адресу 

    `localhost:8000`


### С помощью Docker
1. Из дирректории payments_project запустить команду

`docker-compose up --build`
2. Перейти по адресу

`localhost:8000`

### При возникновении ошибки "exec entrypoint.sh no such file or directory" в файле entrypoint.sh удалить и заново напечатать первую строку, происходит из-за добавления невидимых символов Windows в конец строки