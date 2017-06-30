import logging

log = logging.getLogger(__name__)

__all__ = ['GenericList']

class GenericList(object):
	'''
		Generic list object
	'''

	def __init__(self, name, attributes):
		'''
		name: Name of list element
		attributes: Dictionary containing attributes
	    '''
		super(GenericList, self).__init__()
		self.name = name
		self.attrs = attributes
		self.elements = []


	def addElement(self,element):
		'''
			Add Element to list
		'''

		self.elements.append(element)
		return

	def getElements(self):
		'''
			return list of nodes
		'''
		return self.elements


	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = []

		if self.elements:
			children.extend([n.todict() for n in self.elements])
		return {'tag': self.name, 'children': children, 'attrs': self.attrs }
