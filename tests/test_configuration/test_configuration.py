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

def test_add_section_and_params():
    '''
        Test adding section and params to configuration

    '''
    c = Configuration('conftest.xml', 'Configuration testing')
    c.addParameter('echo-canceller','yes')
    c.addParameter('out-of-band-dtmfs','yes')

    s = Section('test_section')
    p1 = Param('echo-canceller','yes')
    p2 =  Param('out-of-band-dtmfs','no')
    s.addVariable(p1)
    s.addVariable(p2)

    c.addSection(s)
    
    d = c.todict()
    
    assert d['children'][0]['tag'] == 'params'
    assert d['children'][1]['tag'] == 'test_section'
    assert len(d['children']) == 2


def test_add_params():
    '''
        Test adding only params to configuration

    '''
    c = Configuration('conftest.xml', 'Configuration testing')
    c.addParameter('echo-canceller','yes')
    c.addParameter('out-of-band-dtmfs','yes')
    
    d = c.todict()
    
    assert d['children'][0]['tag'] == 'params'
    assert len(d['children']) == 1

def test_add_section():
    '''
        Test adding section to configuration

    '''
    c = Configuration('conftest.xml', 'Configuration testing')
    s = Section('test_section')
    p1 = Param('echo-canceller','yes')
    p2 =  Param('out-of-band-dtmfs','no')
    s.addVariable(p1)
    s.addVariable(p2)

    c.addSection(s)
    
    d = c.todict()
    
    assert d['children'][0]['tag'] == 'test_section'
    assert len(d['children']) == 1

def test_add_sub_section():
    '''
        Test adding section inside another section

    '''
    c = Configuration('conftest.xml', 'Configuration testing')
    global_section = Section('global_section')
    sub_section = Section('sub_section')
    p1 = Param('echo-canceller','yes')
    p2 =  Param('out-of-band-dtmfs','no')
    sub_section.addVariable(p1)
    sub_section.addVariable(p2)
    global_section.addVariable(sub_section)

    c.addSection(global_section)
    
    d = c.todict()

    assert d['children'][0]['tag'] == 'global_section'
    assert d['children'][0]['children'][0]['tag'] == 'sub_section'
    assert len(d['children']) == 1
    assert len(d['children'][0]['children']) == 1

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