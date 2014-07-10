import logging

from wirecurly.dialplan import Extension
from wirecurly.dialplan.condition import Condition

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
        
    def addExtension(self, name):
        '''
            Add a new extension to the context
        '''
        extension = Extension(name)
        self.extensions.append(extension)
        return extension

    def addAbsExtension(self, name):
        '''
            Add a new extension with an absolute condition and return that condition so actions can be added
        '''
        extension = Extension(name)
        self.extensions.append(extension)
        c = Condition()
        extension.addCondition(c)
        return c