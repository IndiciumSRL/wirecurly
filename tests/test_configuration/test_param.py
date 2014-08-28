import logging

from wirecurly.configuration.param import Param
from wirecurly import XMLFileFactory

def test_param():
    '''
        Test param set and its dict representation is correct.
    '''
    p = Param('rtp-start-port', '10000')
    d = p.todict()
    print d
    assert d.has_key('tag'), 'No tag on dict'
    assert d['tag'] == 'param', 'Tag is not correct'
    assert type(d['attrs']) is dict, 'Not a dict...'
    assert d['attrs'].has_key('name'), 'No name for param'
    assert d['attrs']['name'] == 'rtp-start-port', 'name has wrong value'
    assert d['attrs'].has_key('value'), 'No value for param'
    assert d['attrs']['value'] == '10000', 'value attribute has wrong value'