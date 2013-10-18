import logging

log = logging.getLogger(__name__)

__all__ = ['Extension']

class Extension(object):
	""" An extension object for the dialplan """

	def __init__(self,extension):
		super(Extension, self).__init__()
		self.extension = extension
		self.condition = {'field' : 'destination_number' , 'expression' : '^'+ extension +'$'}
		self.actions = []

	def addAction(self,act,val):
		'''
			Set a new action for this extension
		'''
		try:
			self.getAction(act,val)
		except:
			self.actions.append({'application' : act , 'data' : val})
			return

		log.warning('Cannot replace existing action.')
		raise ValueError

	def getCondition(self):
		'''
			Returns value of destination_number condition
		'''
		return self.codition['expression']
		raise ValueError

	def existAction(self,act,val):
		'''
			Return true if an action and data exists 
		'''
		for a in self.actions:
			if a.get('application') == 'act' and a.get('data') == 'val':
				return True
		return False

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		
		children =  {'tag' : 'condition','attrs': self.condition }

		if self.actions:
			children.append({'children': [ {tag : 'action' , attrs : a} for a in self.actions ]})

		return {'tag' : 'extension','children' : children, 'attrs': {'name' : self.extension}}