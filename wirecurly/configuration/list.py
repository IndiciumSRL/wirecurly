import logging

log = logging.getLogger(__name__)

__all__ = ['List']

class List(object):
	'''
		ACL list object
	'''

	def __init__(self,name,default):
		super(List, self).__init__()
		self.attrs = {'name' : name , 'default' : default}
		self.nodes = []


	def addNode(self,node):
		'''
			Add node to list
		'''

		self.nodes.append(node)
		return

	def getNodes(self):
		'''
			return list of nodes
		'''
		return self.nodes


	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = []

		if self.nodes:
			children.extend([n.todict() for n in self.nodes])
		return {'tag': 'list', 'children': children, 'attrs': self.attrs }
