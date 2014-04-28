from wirecurly.dialplan.context import Context

def test_context_serialization():
    '''
        Context needs to be properly serialized.
    '''
    ctx = Context(name="test")
    d = ctx.todict()
    assert d['tag'] == 'context', 'Dict is all wrong %s' % d
    assert isinstance(d['children'], list), 'Dict is all wrong %s' % d
    assert len(d['children']) == 0, 'Dict is all wrong %s' % d