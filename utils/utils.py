import json

from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data