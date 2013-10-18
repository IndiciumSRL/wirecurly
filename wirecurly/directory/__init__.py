import logging

log = logging.getLogger(__name__)

__all__ = ['User']
		
class User(object):
	"""A user object for the directory"""
	def __init__(self, user_id, password):
		super(User, self).__init__()
		self.user_id = user_id
		self.variables = []
		self.parameters = [{'name': 'password', 'value': password}]

	def addVariable(self, var, val):
		'''
			Set an extra variable for an user
		'''
		self.variables.append({'name': var, 'value': val})

	def addParameter(self, param, val):
		'''
			Set an extra parameter for an user
		'''
		self.parameters.append({'name': param, 'value': val})

	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
		children = [{'tag': 'parameters', 'children': [
						{'tag': 'param', 'attrs': p} for p in self.parameters
					]}]
		if self.variables:
			children.append({'tag': 'variables', 'children': [
							{'tag': 'variable', 'attrs': v} for v in self.variables
						]})
		return {'tag': 'user', 'children': children, 'attrs': {'id': self.user_id}}