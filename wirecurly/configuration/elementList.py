import logging

log = logging.getLogger(__name__)

__all__ = ['ElementList']

class ElementList(object):
    '''
		element object to use inside generic lists.
    '''

    def __init__(self, name, attributes):
        '''
        name: element name
        attributes: Dictionary containing attributes
		'''
        super(ElementList, self).__init__()
        self.name = name
        self.attrs = attributes


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        return {'tag': self.name, 'attrs': self.attrs }