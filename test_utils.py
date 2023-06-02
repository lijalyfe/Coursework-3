import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{
        "date": "2019-07-03T18:35:29.512364",
        "description": "Перевод организации",
        "id": 41428829,
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "state": "EXECUTED",
        "to": "Счет 35383033474447895560"
    }]
    assert get_filtered_data(test_data[:2], filter_empty_from=True) == []


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2019-04-04T23:20:05.206878", "2019-03-23T01:09:46.296404"]


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['07.12.2019: Перевод организации\nVisaClassic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD', '19.11.2019: Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.', '13.11.2019: Перевод со счета на счет\nСчет 3861 14** **** 9794 -> Счет **8125\n62814.53 руб.', '30.10.2019: Перевод с карты на счет\nVisaGold 7756 67** **** 2839 -> Счет **9453\n23036.03 руб.', '29.09.2019: Перевод со счета на счет\nСчет 3542 14** **** 9637 -> Счет **4961\n45849.53 USD']
