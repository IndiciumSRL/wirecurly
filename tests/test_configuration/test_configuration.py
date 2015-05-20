import logging

from wirecurly.configuration import *
from wirecurly.configuration.param import *

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

def test_section():
    '''
        Test Section object
    '''
    s = Section('test_section')
    p1 = Param('echo-canceller','yes')
    p2 =  Param('out-of-band-dtmfs','no')
    s.addVariable(p1)
    s.addVariable(p2)
    d_sect = s.todict()
    assert d_sect['tag'] == 'test_section'
    assert d_sect['children'][0]['attrs']['name'] == 'echo-canceller'
    assert d_sect['children'][0]['attrs']['value'] == 'yes'
    assert d_sect['children'][1]['attrs']['name'] == 'out-of-band-dtmfs'
    assert d_sect['children'][1]['attrs']['value'] == 'no'
    assert len(d_sect['children']) == 2