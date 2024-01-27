# Цехановский Ярослав, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def new_order(body): # cоздание заказа
    return requests.post (configuration.URL_SERVICE + configuration.NEW_ORDERS,
                         json=body)


def get_order(track_number): # запрос на получение номера трэка
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


def test_order_data():  # автотест
    response = new_order(data.order_body)

    track_number = response.json()["track"]
    print("Трэк номер заказа:", track_number)


    order_response = get_order(track_number) # получение данных заказа по номеру треку

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)