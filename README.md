## Цехановский Ярослав, 12-я когорта - дипломный проект, 2-я часть
###  Работа с базой данных

####  Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

####  Ответ:

код запроса

          SELECT c.login, COUNT(*) AS order_count
              FROM "Orders" AS o
              INNER JOIN "Couriers" AS c ON o."courierId" = c.id
              WHERE o."inDelivery" = true
              GROUP BY c.login ;

####  Результат запроса представлен на скриншоте [sql-запрос1.jpg](https://github.com/Jaroslav1984/11sprint_test/blob/main/sql-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%811.jpg)



####  Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.


####  Ответ:

код запроса

      SELECT track,
               CASE
              WHEN finished = true THEN 2
              WHEN cancelled = true THEN -1
              WHEN "inDelivery" = true THEN 1
          ELSE 0 END AS status
          FROM "Orders" ;

####  Результат запроса представлен на скриншоте [sql-запрос2.jpg](https://github.com/Jaroslav1984/11sprint_test/blob/main/sql-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%812.jpg)

##### Коды запросов по 1 и 2 заданию также продублированы здесь: [ЗапросыSQL.txt](https://github.com/Jaroslav1984/11sprint_test/blob/main/%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8BSQL.txt)



###  Автоматизация теста к API

####  Задание


Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.



####  Ответ:

Файлы в репозитории для использования в автотесте в Pycharm: [data.py](https://github.com/Jaroslav1984/11sprint_test/blob/main/data.py), [configuration.py](https://github.com/Jaroslav1984/11sprint_test/blob/main/configuration.py), [sender_stand_request.py](https://github.com/Jaroslav1984/11sprint_test/blob/main/sender_stand_request.py)


URL используемый в запросах - https://{id}.serverhub.praktikum-services.ru

Код автотеста представлен здесь [sender_stand_request.py](https://github.com/Jaroslav1984/11sprint_test/blob/main/sender_stand_request.py)

####  Результат автотеста представлен на скриншоте [autotest.jpg](https://github.com/Jaroslav1984/11sprint_test/blob/main/autotest.jpg)

