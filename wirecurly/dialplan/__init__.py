import logging
import condition

log = logging.getLogger(__name__)

__all__ = ['Extension']

class Extension(object):
	""" An extension object for the dialplan """

	def __init__(self,extension):
		super(Extension, self).__init__()
		self.extension = extension
		self.conditions = [] 
	
	def addCondition(self,cond):
		'''
			Add a condition for this extension
		'''

		if type(cond.todict()) != list:
			try:	
				self.getCondition(cond)
			except ValueError: #Condition doesnt exist
				self.conditions.append(cond)
				return
			log.warning('Cannot replace existing condition')
			raise ValueError
		else: # We have to check all conditions in list
			for c in cond.todict():
				try:
					self.getCondition(c)
				except ValueError:
					self.conditions.append(c)
				else:
					log.warning('Cannot replace existing condition')
					raise ValueError
					return

		

	def getCondition(self,cond):
		'''
			Returns a condition object based on its attributes
		'''
		for c in self.conditions:
			if type(c) == type(cond):
				if c.attrs == cond.attrs:
					return c
		raise ValueError

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = [] 

		if self.conditions:


			for c in self.conditions:
				if type(c.todict()) == dict: #Condition could be a dict (Class condition) ...
					children.append(c.todict())
				elif type(c.todict()) == list: # or a list of conditions (Classes or_ , and_) .
					for cond in c.todict():
						children.append(cond.todict())



		return {'tag': 'extension', 'children': children, 'attrs': {'name': self.extension}}
		