import logging

log = logging.getLogger(__name__)

__all__ = ['Gateway']
		
class Gateway(object):
	"""A gateway object"""
	def __init__(self, name):
		super(Gateway, self).__init__()
		self.name = name
		self.parameters = []


	def addParameter(self, param, val):
		'''
			Set an extra parameter for a gateway
		'''
		try:
			self.getParameter(param)
		except ValueError:
			self.parameters.append({'name': param, 'value': val})
			return
		
		log.warning('Cannot replace existing parameter.')
		raise ValueError

	def getParameter(self, param):
		'''
			Retrieve the value of a parameter by its name
		'''
		for p in self.parameters:
			if p.get('name') == param:
				return p.get('value')

		raise ValueError


	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		if self.parameters:
			children =[{'tag': 'param', 'attrs': p} for p in self.parameters]
		
	
		return {'tag': 'gateway', 'children': children, 'attrs': {'name': self.name}}