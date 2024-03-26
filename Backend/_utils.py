"""
defines the utils used
"""
import re
def ensure_type(obj, type: type | tuple, errmsg=None):
    '''ensure obj is of a certain type'''
    if isinstance(obj, type):
        return 1
    if not errmsg:
        return f'type of{obj} is not of instance {type}'
    return errmsg

def valid_url(url):
    """validates url"""
    