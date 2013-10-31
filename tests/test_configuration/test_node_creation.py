'''
	Test node creation for acls
'''

import unittest
from wirecurly.configuration import node
from nose import tools


class testNodeCreation(unittest.TestCase):
	'''
		Test node creation
	'''

	def setUp(self):
		'''
			Node fixtures for tests
		'''

		self.node = node.Node('allow','100.100.100.100/32')
		
	def test_node_dict_ok(self):
		'''
			Test that node is properly serialized 
		'''
		assert isinstance(self.node.todict(), dict)

	