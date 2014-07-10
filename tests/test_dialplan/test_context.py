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

def test_context_extension_creation():
    '''
    Test adding extensions to the context.
    '''
    ctx = Context(name="test")
    extension = ctx.addExtension("Test extension")
    assert len(ctx.extensions) == 1, "No extension was added to internal state."
    assert extension == ctx.extensions[len(ctx.extensions)-1], "Extension was not added on the proper place."