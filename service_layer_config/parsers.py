"""
A collection of parsers that should match those listed in the config.yml file.

Each parser must be added ans an entrypoint. This allows MSL plugins that only
define parsers.
"""

import simplejson as json


def parser_example(data):
    """Manipulate incoming data and return the modified data."""
    return data


def _data_zero(data):
    print('data[0]:')
    print(data[0])
    print('data[0].keys:')
    print(data[0].keys())


def addresses_json_generator(data):
    """Strip names and addresses from this source format."""
    data = json.loads(data)
    _data_zero(data)
    data = [('{first} {last}'.format(**x['name']),
            str(x['address']))
            for x in data]
    return data


def addresses_filltext(data):
    """Strip names and addresses from this source format."""
    data = json.loads(data)
    _data_zero(data)
    data = [('{fname} {lname}'.format(**x),
            '{address}, {city}, {state} {zip}'.format(**x))
            for x in data]
    return data
