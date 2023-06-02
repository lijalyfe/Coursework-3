import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)