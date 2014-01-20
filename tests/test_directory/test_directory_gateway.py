import logging

import pytest
from lxml import etree
from mock import Mock

from wirecurly.directory import Gateway

def test_gateway():
    '''
    Test gateway creation
    '''
    gateway = Gateway('Test')
    d = gateway.todict()
    assert d['tag'] == 'user'
    assert d['attrs']['id'] == 'Test'
    assert d['children'][0]['tag'] == 'gateways'
    assert d['children'][0]['children'][0]['tag'] == 'gateway'
    assert d['children'][0]['children'][0]['children'][0]['tag'] == 'params'
    assert not d['children'][0]['children'][0]['children'][0]['children']
    gateway.addParameter('context', 'default')
    d = gateway.todict()
    assert len(d['children'][0]['children'][0]['children'][0]['children']) == 1
    with pytest.raises(ValueError):
        gateway.addParameter('context', 'default')