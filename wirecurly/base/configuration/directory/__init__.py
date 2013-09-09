from wirecurly.base.configuration import Document, Section
from wirecurly.base import Element

class Params(Element):
	"""Parameters entry"""
	def __init__(self):
		super(Params, self).__init__('params')

class Param(Element):
	"""Param entry"""
	def __init__(self, name, value):
		super(Param, self).__init__('param', name=name, value=value)
		self.name = name
		self.value = value
		
class Groups(Element):
	"""Groups to be established"""
	def __init__(self):
		super(Groups, self).__init__('groups')

class Group(Element):
	"""A directory group"""
	def __init__(self, name):
		super(Group, self).__init__('group', name=name)
		self.name = name
		
class Users(Element):
	"""Users tag"""
	def __init__(self):
		super(Users, self).__init__('users')
		

class User(Element):
	"""A user element"""
	def __init__(self, id):
		super(User, self).__init__('user', id=id)
		self.id = id
		
class Variables(Element):
	"""Variables tag"""
	def __init__(self):
		super(Variables, self).__init__('variables')

class Variable(Element):
	"""A variable tag"""
	def __init__(self, name, value):
		super(Variable, self).__init__('variable', name=name, value=value)
		self.name = name
		self.value = value
		
class Gateways(Element):
	"""Gateways tag"""
	def __init__(self):
		super(Gateways, self).__init__('gateways')
		
class Gateway(Element):
	"""Gateway tag"""
	def __init__(self, name):
		super(Gateway, self).__init__('gateway', name=name)
		self.name = name
		
class Domain(Element):
	"""A domain for a directory entry"""
	def __init__(self, name):
		super(Domain, self).__init__('domain', name=name)

class Directory(Document):
	"""A root directory"""
	def __init__(self, domain=None):
		super(Directory, self).__init__(Section('directory'))
		if domain is not None:
			self[0] = Domain(domain)

	def setDomain(self, domain):
		''' Set the domain '''
		domainObj = Domain(domain)
		self[0] = domainObj
		return domainObj

	def getDomain(self):
		''' Return the domain object '''
		return self[0][0]