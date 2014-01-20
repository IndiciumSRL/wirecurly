'''
	Test gateway creation
'''

import unittest
from wirecurly.configuration import gateway
import pytest


class testGatewayCreation(unittest.TestCase):
	'''
		Test gateway creation
	'''

	def setUp(self):
		'''
			gateway fixtures for tests
		'''

		self.gw = gateway.Gateway('name')

		
	def test_gw_dict_ok(self):
		'''
			Test that gw is properly serialized 
		'''
		self.gw.addParameter('username','someuser')
		assert isinstance(self.gw.todict(), dict)

	def test_adding_param(self):
		'''
			Test if param is properly add to a gateway
		'''
		self.gw.addParameter('username','someuser') 
		assert self.gw.getParameter('username') == 'someuser'

	def test_adding_existing_param(self):
		'''
			Test adding an existing param
		'''
		with pytest.raises(ValueError):
			self.gw.addParameter('username','someuser')
			self.gw.addParameter('username','someuser')

		