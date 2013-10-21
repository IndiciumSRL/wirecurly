'''
	Test extension creation for dialplan
'''

import unittest
from wirecurly import dialplan
from nose import tools

class testExtensionCreation(unittest.TestCase):
	'''
		Test extension creation
	'''

	def setUp(self):
		'''
			Extension fixtures for tests
		'''

		self.ext = dialplan.Extension('1000')
		
	def test_extension_dict_ok(self):
		'''
			Test that extension is properly serialized 
		'''
		assert isinstance(self.ext.todict(), dict)

	def test_adding_condition(self):
		'''
			Test if an action is properly add to a condition
		'''
		self.ext.addCondition('destination_number','1000')
		assert self.cond.getAction('destination_number','1000')

	@tools.raises(ValueError)
	def test_adding_existing_action(self):
		'''
			Test adding an existing action
		'''
		self.ext.addCondition('answer','')
		self.ext.addCondition('answer','')