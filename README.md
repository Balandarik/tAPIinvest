# tAPIinterface

Неофициальный интерфейс для работы с Tinkoff Invest OpenApi v2 по протоколу Rest. Перед началом работы ознакомьтесь с
официальной документацией [Swagger](https://tinkoff.github.io/investAPI/swagger-ui/).

# Начало работы

Для установки необходимо скачать код из репозитория и запустить скрипт setup.py

    git clone https://github.com/balandarik/tAPIinvest
    python setup.py install

Проверка работы пакета

    from client.tests.tests import *
    client.tests.start_tests()
    

В сервисе реализовано 2 класса для работы с боевым режимом и режимом песочницы

> main_function - боевой режим
>
> sandbox - режим песочницы

Дальнейшая работа реализована при первоначальном определении класса и передачи классу токена аутентификации:

    f=main_function('/your token here/')

# Токен аутентификации

Получить токен аутентификации можно в личном кабинете [Тинькофф Инвестиций](https://www.tinkoff.ru/invest/).

# Связь с разработчиком

Если у вас есть предложения по улучшению кода данного проекта, можете написать в issues.

# Пример использования сервиса

    #Получение списка облигаций

    from client.tAPIinvest import *
    token='/token here/'
    f=main_function(token)
    bonds=f.bonds()
    print(bonds)

    #Получение размера гарантийного обеспечения по фьючерсам

    from client.tAPIinvest import *
    token='/token here/'
    f=main_function(token)
    futures_margin=f.GetFuturesMargin(figi='FUTMOEX03220')
    print(futures_margin)
    
    