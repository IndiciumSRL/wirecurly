import logging

log = logging.getLogger(__name__)

__all__ = ['GenericList']

class GenericList(object):
	'''
		Generic list object
		Receives a dictionary with its attributes
		Dictionary must contain a key called 'list_name' to be used as name of the list
		ex: {'list_name': 'agents', 'name': 'example'} will be parsed as <agents name='example'>
	'''

	def __init__(self, attributes):
		super(GenericList, self).__init__()
		self.list_name = attributes.get('list_name')
		attributes.pop('list_name')
		self.attrs = attributes
		self.elements = []


	def addElement(self,element):
		'''
			Add Element to list
		'''

		self.nodes.append(element)
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
		return {'tag': self.list_name, 'children': children, 'attrs': self.attrs }
