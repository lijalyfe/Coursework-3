import json

from datetime import datetime


def get_data():
    '''Чтение данных из файла operations.json.'''
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_filtered_data(data, filter_empty_from=False):
    '''Фильтрация данных из файла operations.json.'''
    data = [d for d in data if 'state' in d and d['state'] == 'EXECUTED']
    if filter_empty_from:
        data = [d for d in data if 'from' in d]
    return data


def get_last_values(data, count_last_values):
    '''Сортировка данных по дате'''
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    '''Форматирование данных для вывода в консоль'''
    formatted_data = []
    for row in data:
        data = datetime.strptime(row['date'],'%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        racipient = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        if 'from' in row:
            sender = row['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[-4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = ''.join(sender)
        else:
            from_info, from_bill = '', ''
        formatted_data.append(f"""\
{date}: {description}
{from_info} {from_bill} -> {racipient}
{operations_amount}""")
    return formatted_data



