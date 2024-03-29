import codecs
import os
import sys
from pdb import set_trace


def read_file(path, encoding='utf-8'):
    """Reads the file at the target path.
    """
    fobj = codecs.open(path, "r", encoding=encoding)
    try:
        contents = fobj.read()
    except UnicodeDecodeError, e:
        # re-raise with more information
        raise Exception('%s: %s' % (e, path))
    finally:
        fobj.close()
    return contents


def read_json_file(path):
    """ Returns the JSON contents at the specified path. """
    if not path.endswith('.json'):
        path += '.json'
    # get the json file
    full_path = os.path.join(os.path.abspath('.'), 'loremjson', 'static', 'json', path)
    # return full_path
    return read_file(full_path)