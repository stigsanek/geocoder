import requests
from modules.util import parse_file, parse_result, write_data

def run_geocoder(api_key, is_reverse):
    data = parse_file(is_reverse)
    output_data = []
    errors = []

    string_query = f'https://geocode-maps.yandex.ru/1.x/?&apikey={api_key}&format=json&geocode='

    for item in data:
        line_id, param, src_line = item['id'], item['param'], item['src_line']
        query = string_query + param

        try:
            response = requests.get(query)
        except requests.ConnectionError:
            print(f'Network error on at string: {line_id}')
            errors += [src_line]
        if response.status_code == 200:
            result = response.json()
            addr = parse_result(is_reverse, item['id'], result)
            print(f'Processed: {line_id}')
            output_data.append(addr)
        else:
            print(f'Server error on at string: {line_id}')
            errors += [src_line]

    write_data('output', output_data) if len(output_data) > 0 else False
    write_data('error', errors) if len(errors) > 0 else False
    print('Successfully processed:', len(output_data))
    print('Handled with error:', len(errors))
