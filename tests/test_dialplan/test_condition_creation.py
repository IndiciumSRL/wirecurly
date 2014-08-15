'''
	Test condition creation for dialplan
'''

import unittest
from wirecurly.dialplan import condition
from wirecurly.dialplan.expression import *

class AppMock(object):
	"""An application interface mockup"""
	def __init__(self):
		super(AppMock, self).__init__()
		self.app_name = 'test'
		self.data = ''


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

	def test_condition_anti_action_dict_ok(self):
		'''
			Test that condition with an anti-action is properly serialized
		'''
		self.cond.addAntiAction('answer','')
		assert isinstance(self.cond.todict(), dict)

	def test_condition_action_anti_action_dict_ok(self):
		'''
			Test that condition with an action and an anti-action is properly serialized
		'''
		self.cond.addAction('answer','')
		self.cond.addAntiAction('hangup','')
		assert isinstance(self.cond.todict(), dict)

	def test_adding_action(self):
		'''
			Test if an action is properly add to a condition
		'''
		self.cond.addAction('answer','')
		assert self.cond.existAction('answer','')

	def test_adding_action_inline(self):
		'''
			Test if an action with inline=True is properly add to a condition
		'''
		self.cond.addAction('answer','', True)
		assert self.cond.existAction('answer','', True)

	def test_adding_anti_action(self):
		'''
			Test if an anti-action is properly add to a condition
		'''
		self.cond.addAntiAction('hangup','')
		assert self.cond.existAntiAction('hangup','')

	def test_adding_application(self):
		'''
			Test adding an application to a Condition
		'''
		self.cond.addApplication(AppMock())
		assert self.cond.existAction('test', '')

	def test_adding_application_inline(self):
		'''
			Test adding an application with inline=True to a Condition
		'''
		self.cond.addApplication(AppMock(), True)
		assert self.cond.existAction('test', '', True)
		
	def test_adding_existing_action(self):
		'''
			Test adding an existing action
		'''
		self.cond.addAction('answer','')
		self.cond.addAction('answer','')

class testOrConditionCreation(unittest.TestCase):
	'''
		Test conditions creation with logical or
	'''

	def setUp(self):
		'''
			Or Condition fixtures for tests
		'''
		self.cond1 = condition.Condition(expr=ExpressionTime('mon-fri','9-18'))
		self.cond2 = condition.Condition(expr=ExpressionTime('sat','9-13'))
		self.orcond = condition.or_(self.cond1,self.cond2)
		
	def test_condition_list_ok(self):
		'''
			Test that condition is properly serialized 
		'''
		assert isinstance(self.orcond.todict(), list)

	
