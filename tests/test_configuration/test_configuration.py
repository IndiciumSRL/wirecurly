import logging

from wirecurly.configuration import *
from wirecurly import XMLFileFactory

def test_configuration():
    '''
        Test configuration object.
    '''
    c = Configuration('conftest.xml', 'Configuration testing')
    c.addParameter('echo-canceller','yes')
    c.addParameter('out-of-band-dtmfs','yes')
    d = c.todict()

    assert d['attrs']['description'] == 'Configuration testing'
    assert d['attrs']['name'] == 'conftest.xml'
    assert len(d['children'][0]) == 2