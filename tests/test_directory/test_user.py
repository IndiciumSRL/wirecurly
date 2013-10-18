'''
	Test the creation of a user on the directory
'''

import unittest
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

