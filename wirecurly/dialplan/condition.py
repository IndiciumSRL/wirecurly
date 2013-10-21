import logging

log = logging.getLogger(__name__)

__all__ = ['Condition']

class Condition(object):
	'''
		Condition oject for dialplan
	'''

	def __init__(self,cond,val):
		super(Condition, self).__init__()
		self.attrs = {'field' : cond , 'expression' : val}
		self.actions = []

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

	def existAction(self,act,val):
			'''
				Return true if an action and data exists 
			'''
			for a in self.actions:
				if a.get('application') == act and a.get('data') == val:
					return True
			return False

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = []

		if self.actions:
			children.append([[{'tag': 'action', 'attrs': a} for a in self.actions]])
		
		return {'tag': 'condition', 'children': children, 'attrs': self.attrs }