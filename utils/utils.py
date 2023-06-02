import json

from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_filtered_data(data, filter_empty_from=False):
    data = [d for d in data if 'state' in d and d['state'] == 'EXECUTED']
    if filter_empty_from:
        data = [d for d in data if 'from' in d]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data
