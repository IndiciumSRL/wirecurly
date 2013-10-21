import logging
from wirecurly.exc import *

log = logging.getLogger(__name__)

__all__ = ['Condition','TimeCondition','AbsoluteCondition']

class Condition(object):
	'''
		Condition oject for dialplan
	'''

	def __init__(self,cond,val):
		super(Condition, self).__init__()
		self.attrs = {'field' : cond , 'expression' : val}
		self.actions = []
		self.antiactions = []

	def addAction(self,act,val):
			'''
				Set a new action for this condition
			'''
			if not self.existAction(act,val):
				self.actions.append({'application' : act , 'data' : val})	
			else:
				log.warning('Cannot replace existing action.')
				raise ValueError
			return

	def addAntiAction(self,act,val):
			'''
				Set a new anti-action for this condition
			'''
			if not self.existAntiAction(act,val):
				self.antiactions.append({'application' : act , 'data' : val})	
			else:
				log.warning('Cannot replace existing anti-action.')
				raise ValueError
			return

	def addApplication(self, app):
		'''
			Add an application.
			An application must have 2 attributes. app_name and data.
		'''
		if not hasattr(app, 'app_name') or not hasattr(app, 'data'):
			raise NoSuchApplication
		else:
			self.addAction(app.app_name, app.data)

	def existAction(self,act,val):
			'''
				Return true if an action and data exists 
			'''
			for a in self.actions:
				if a.get('application') == act and a.get('data') == val:
					return True
			return False

	def existAntiAction(self,act,val):
			'''
				Return true if an antiaction and data exists 
			'''
			for a in self.antiactions:
				if a.get('application') == act and a.get('data') == val:
					return True
			return False

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = []

		if self.actions:
			children.extend([{'tag': 'action', 'attrs': a} for a in self.actions])

		if self.antiactions:
			children.extend([{'tag': 'anti-action', 'attrs': a} for a in self.antiactions])
			
		return {'tag': 'condition', 'children': children, 'attrs': self.attrs }

class TimeCondition(Condition):
	'''
		Time Condition oject for dialplan
	'''

	def __init__(self,wday,hour):
		#super(TimeCondition, self).__init__()
		self.attrs = {'wday' : wday , 'hour' : hour}
		self.actions = []
		self.antiactions = []

class AbsoluteCondition(Condition):
	'''
		Absolute Condition oject for dialplan
	'''

	def __init__(self):
		#super(AbsoluteCondition, self).__init__()
		self.attrs = {}
		self.actions = []
		self.antiactions = []
