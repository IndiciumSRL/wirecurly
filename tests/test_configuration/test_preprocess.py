import logging

from wirecurly.configuration.preprocess import PreprocessSet

def test_preprocess_set():
    '''
        Test preprocess set and its dict representation is correct.
    '''
    pp = PreprocessSet('test', '123')
    d = pp.todict()
    assert d.has_key('tag'), 'No tag on dict'
    assert d['tag'] == 'X-PRE-PROCESS', 'Tag is not correct'
    assert type(d['attrs']) is dict, 'Not a dict...'
    assert d['attrs'].has_key('cmd'), 'No command set on preprocess directive'
    assert d['attrs']['cmd'] == 'set', 'Cmd attribute has wrong value'
    assert d['attrs'].has_key('data'), 'No data set on preprocess directive'
    assert d['attrs']['data'] == 'test=123', 'Data attribute has wrong value'
