'''
	Test condition creation for dialplan
'''

import unittest
from wirecurly.dialplan import condition
from nose import tools

class testConditionCreation(unittest.TestCase):
	'''
		Test condition creation
	'''

	def setUp(self):
		'''
			Condition fixtures for tests
		'''

		self.cond = condition.Condition('destination_number','1000')
		
	def test_condition_dict_ok(self):
		'''
			Test that condition is properly serialized 
		'''
		assert isinstance(self.cond.todict(), dict)

	def test_condition_action_dict_ok(self):
		'''
			Test that condition with an action is properly serialized
		'''
		self.cond.addAction('answer','')
		assert isinstance(self.cond.todict(), dict)


	def test_adding_action(self):
		'''
			Test if an action is properly add to a condition
		'''
		self.cond.addAction('answer','')
		assert self.cond.existAction('answer','')
		
	@tools.raises(ValueError)
	def test_adding_existing_action(self):
		'''
			Test adding an existing action
		'''
		self.cond.addAction('answer','')
		self.cond.addAction('answer','')

