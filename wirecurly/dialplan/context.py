import logging

log = logging.getLogger(__name__)

__all__ = ['Context']

class Context(object):
    """A dialplan context"""
    def __init__(self, name):
        super(Context, self).__init__()
        self.name = name
        self.extensions = []

    def todict(self):
        '''
            Serialize context and its extensions to dicts.
        '''
        children = []
        if self.extensions:
            for c in self.extensions:
                children.append(c.todict())

        return {'tag': 'context', 'children': children, 'attrs': {'name': self.name}}
        