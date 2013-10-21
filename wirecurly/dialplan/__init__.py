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
		try:
			self.getCondition(cond.attrs['field'],cond.attrs['expression'])
		except ValueError:
			self.conditions.append(cond)
			return

		log.warning('Cannot replace existing condition')
		raise ValueError

	def addAbsoluteCondition(self,cond):
		'''
			Add an absolute condition for this extension
		'''
		self.conditions.append(cond)

	def addTimeCondition(self,cond):
		'''
			Add a time condition for this extension
		'''
		try:
			self.getTimeCondition(cond.attrs['wday'],cond.attrs['hour'])
		except ValueError:
			self.conditions.append(cond)
			return

		log.warning('Cannot replace existing condition')
		raise ValueError

	def getCondition(self,field,exp):
		'''
			Returns a condition object
		'''
		for c in self.conditions:
			if c.attrs['field'] == field and c.attrs['expression'] == exp:
				return c
		raise ValueError 

	def getTimeCondition(self,week,hour):
		'''
			Returns a time condition object
		'''
		for c in self.conditions:
			try:
				if c.attrs['wday'] == week and c.attrs['hour'] == hour:
					return c
			except KeyError:
				pass
		raise ValueError 

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = [] 

		if self.conditions:
			for c in self.conditions:
				children.append(c.todict())
	
		return {'tag': 'extension', 'children': children, 'attrs': {'name': self.extension}}
		