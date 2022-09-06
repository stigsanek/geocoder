from collections import OrderedDict

from geocoder.config import CSV_DIR
from geocoder.logger import logger


def create_param(is_reverse, data):
    """Creates parameter"""
    line_id = data[0]

    try:
        if is_reverse:
            param = data[1]
            src_line = [data[0], data[1]]
        else:
            param = data[1] + ',' + data[2]
            src_line = [data[0], data[1], data[2]]

        return {'id': line_id, 'param': param, 'src_line': src_line}
    except Exception as err:
        logger.error(f'Create param error: {err}')


def parse_file(is_reverse):
    """Parses file"""
    input_data = []

    with open(CSV_DIR / 'input.csv', encoding='utf-8') as input_file:

        for line in input_file:
            data = line.split(';')
            new_data = []

            for item in data:
                new_data.append(item.strip())

            param = create_param(is_reverse, new_data)
            input_data.append(param)

    return input_data


def parse_result(is_reverse, line_id, resp):
    """Parses result"""
    try:
        data = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        address_data = get_address_components(data)
        address = list(address_data.values())

        if is_reverse:
            coord = data['Point']['pos']
            return [line_id] + coord.split() + address
        else:
            return [line_id] + address
    except Exception:
        return [line_id] + ['Н/Д']


def get_address_components(data):
    """Returns address components"""
    result = OrderedDict()
    result['country'] = None
    result['province'] = None
    result['area'] = None
    result['locality'] = None
    result['street'] = None
    result['house'] = None

    for key in result.keys():
        for component in data['metaDataProperty']['GeocoderMetaData']['Address']['Components']:
            if component['kind'] == key:
                if result[key]:
                    result[key] += ';' + component['name']
                else:
                    result[key] = component['name']

    return result


def write_data(file, data):
    """Writes data to file"""
    with open(CSV_DIR / f'{file}.csv', 'a', encoding='utf-8') as output_file:
        for item in data:
            filter_data = tuple(filter(lambda i: isinstance(i, str), item))
            line = ';'.join(filter_data)
            output_file.write(line + '\n')
