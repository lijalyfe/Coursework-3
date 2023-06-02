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

