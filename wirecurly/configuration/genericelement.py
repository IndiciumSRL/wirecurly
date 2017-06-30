import logging

log = logging.getLogger(__name__)

__all__ = ['GenericElement']

class GenericElement(object):
    '''
		Generic element object
    '''

    def __init__(self, name, attributes={}):
        '''
        name: element name
        attributes: Dictionary containing attributes
		'''
        super(GenericElement, self).__init__()
        self.name = name
        self.attrs = attributes

    def addAttr(self, attr, val):
		'''
			Add an attribute to element
		'''
		try:
			self.getAttr(attr)
		except ValueError:
			self.attributes[attr] = val
			return
		log.warning('Cannot modify existing attribute')
		raise ValueError


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        return {'tag': self.name, 'attrs': self.attrs }