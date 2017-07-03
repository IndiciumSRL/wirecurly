import logging

log = logging.getLogger(__name__)

__all__ = ['GenericElement']

class GenericElement(object):
    '''
		Generic element object
    '''

    def __init__(self, name, attributes={}, elements=[]):
        '''
        name: element name
        attributes: Dictionary containing attributes
		'''
        super(GenericElement, self).__init__()
        self.name = name
        self.attrs = attributes
        self.elements = elements

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

    def addElement(self, element):
        '''
            Add a subelement to GenericElement. This object must contain a todict method.
        '''
        self.elements.append(element)


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''

        if self.elements:
            children = [v.todict() for v in self.elements]
            return {'tag': self.name, 'attrs': self.attrs, 'children': children}
        else:
            return {'tag': self.name, 'attrs': self.attrs}
