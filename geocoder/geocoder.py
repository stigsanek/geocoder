import requests

from .logger import logger
from .util import parse_file, parse_result, write_data


def run_geocoder(api_key, is_reverse):
    data = parse_file(is_reverse)
    outputs = []
    errors = []

    str_query = f'https://geocode-maps.yandex.ru/1.x/?&apikey={api_key}&format=json&geocode='

    for item in data:
        global line_id, src_line, query

        try:
            line_id, param, src_line = item['id'], item['param'], item['src_line']
            query = str_query + param
        except Exception as err:
            logger.error(f'Invalid input data. Error: {err}')
            exit()

        try:
            response = requests.get(query)

            if response.status_code == 200:
                result = response.json()
                address = parse_result(is_reverse, item['id'], result)

                logger.info(f'Processed: {line_id}')

                outputs.append(address)
                write_data('output', [address])
            else:
                logger.error(f'Server error on at string: {line_id}')

                errors.append(src_line)
                write_data('error', [src_line])
        except requests.ConnectionError:
            logger.error(f'Network error on at string: {line_id}')

            errors.append(src_line)
            write_data('error', [src_line])

    logger.info(f'Successfully processed: {len(outputs)}')
    logger.info(f'Handled with error: {len(errors)}')
