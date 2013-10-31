import logging

log = logging.getLogger(__name__)

__all__ = ['Node']

class Node(object):
	'''
		Node oject for acls
	'''

	def __init__(self,perm,add):
		super(Node, self).__init__()
		self.attrs = {'type' : perm , 'cidr' : add}
		
	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		return {'tag': 'node', 'attrs': self.attrs }
