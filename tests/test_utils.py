import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data():
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
        "state": "EXECUTED"
        "to": "Счет 35383033474447895560"
    }]
    assert get_filtered_data(test_data[:2], filter_empty_from=True) == []

