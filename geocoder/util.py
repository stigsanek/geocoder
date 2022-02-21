import os

from collections import OrderedDict


def create_param(is_reverse, data):
    line_id = data[0]

    try:
        if is_reverse:
            param = data[1]
            src_line = [data[0], data[1]]
        else:
            param = data[1] + ',' + data[2]
            src_line = [data[0], data[1], data[2]]

        return {'id': line_id, 'param': param, 'src_line': src_line}
    except Exception:
        pass


def parse_file(is_reverse):
    input_data = []
    file_name = os.path.join('csv', 'input.csv')

    with open(file_name, encoding='utf8') as input_file:

        for line in input_file:
            data = line.split(';')
            new_data = []

            for item in data:
                new_data.append(item.strip())

            param = create_param(is_reverse, new_data)
            input_data.append(param)

    return input_data


def parse_result(is_reverse, line_id, resp):
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
    file_name = os.path.join('csv', f'{file}.csv')

    with open(file_name, 'a', encoding='utf8') as output_file:
        for item in data:
            filter_data = tuple(filter(lambda i: isinstance(i, str), item))
            line = ';'.join(filter_data)
            output_file.write(line + '\n')
