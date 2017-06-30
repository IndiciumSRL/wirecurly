import logging

log = logging.getLogger(__name__)

__all__ = ['ElementList']

class ElementList(object):
    '''
		element object to use inside generic lists.

		Dictionary must contain a key called 'element_name' to be used as name of the element
		ex: {'element_name': 'agent', 'name': 'example'} will be parsed as <agent name='example'>
    '''

    def __init__(self, attributes):
        super(ElementList, self).__init__()
        self.element_name = attributes.get('element_name')
        attributes.pop('element_name')
        self.attrs = attributes


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        return {'tag': self.element_name, 'attrs': self.attrs }