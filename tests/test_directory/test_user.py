'''
	Test the creation of a user on the directory
'''

import unittest
import pytest
from wirecurly import directory

class testUserCreation(unittest.TestCase):
	"""Test user creation"""
	def setUp(self):
		'''
			Create our fixtures for these tests
		'''
		self.user = directory.User('1000', 'this is a test')

	def test_user_is_can_be_a_dict(self):
		'''
			Test that our user can be properly serialized
		'''
		assert isinstance(self.user.todict(), dict)

	def test_adding_parameter_to_user(self):
		'''
			Test adding a parameter to a user
		'''
		self.user.addParameter('vm-password', '123')
		assert self.user.getParameter('vm-password') == '123'

	def test_adding_variable_to_user(self):
		'''
			Test adding a variable to a user
		'''
		self.user.addVariable('toll-allow', 'intl')
		assert self.user.getVariable('toll-allow') == 'intl'

	def test_adding_existing_variable(self):
		'''
			Test trying to replace an existing variable
		'''
		with pytest.raises(ValueError):
			self.user.addVariable('test', 'intl')
			self.user.addVariable('test', 'intl')

	def test_adding_existing_parameter(self):
		'''
			Test trying to replace an existing parameter
		'''
		with pytest.raises(ValueError):
			self.user.addParameter('password', 'anything')
