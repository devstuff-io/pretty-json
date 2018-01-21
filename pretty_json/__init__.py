from __future__ import absolute_import

try:
    import simplejson as json
except ImportError:
    import json

from datetime import datetime

from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.styles import get_all_styles
from pygson.json_lexer import JSONLexer

from pretty_json.settings import OUTPUT_STYLE


AVAILABLE_STYLES = list(get_all_styles())


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code

    :param obj: **required**. Ensures obj can be json serializable.
    """
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial


def jdump(obj, *args, **kwargs):
    rtn = None
    try:
        rtn = json.dumps(obj, encoding='latin1', default=json_serial, **kwargs)
    except TypeError:
        rtn = json.dumps(obj, default=json_serial, **kwargs)
    except:
        raise
    return rtn


def pretty_print(obj, sort_keys=True, indent=4, separators=(',', ': ')):
    """Pretty prints json object.

    :param obj: **required**. The json.
    :type obj: dict/json.
    :param sort_keys: Sort the keys.
    :type sort_keys: bool.
    :param indent: Indent each depth by n * int.
    :type indent: int.
    :param separators: element separators
    :type separators: set.
    :return: str
    """
    return jdump(obj, sort_keys=sort_keys, indent=indent, separators=separators)


def format_json(content, style=OUTPUT_STYLE):
    """Prettify JSON.

    :param content: **required**.
    :type content: json.
    """
    return highlight(
        pretty_print(content, sort_keys=False),
        JSONLexer(),
        Terminal256Formatter(style=style)
    ).strip()


def sample(style=OUTPUT_STYLE):
    print(format_json({
        'AVAILABLE_STYLES': AVAILABLE_STYLES,
        'types': {
            'int': 42,
            'float': 8.75,
            'dict': {
                'foo': {
                    'str': 'this is a string'
                }
            }
        }
    }, style))


__version__ = '1.2.0'
