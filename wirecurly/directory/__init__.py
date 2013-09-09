import logging

from wirecurly.base import Element
from wirecurly.base.configuration import Document, Section
from wirecurly.base.configuration import directory

log = logging.getLogger(__name__)

__all__ = ['notfound', 'Directory']
		
class Result(Element):
	"""The result to be used when something was not found"""
	def __init__(self):
		super(Result, self).__init__('result', status='not found')
		

class User(object):
	"""Represents a user on the directory"""
	def __init__(self, id):
		super(User, self).__init__()
		self.id = id
		self.user = directory.User(id)
		self.params = directory.Params()
		self.variables = directory.Variables()
		self.user.addChild(self.params)
		self.user.addChild(self.variables)

	def addParam(self, key, value):
		self.params.addChild(directory.Param(key, value))

	def addVariable(self, key, value):
		self.variables.addChild(directory.Variable(key, value))

class Gateway(object):
	"""Represents a high level absctration of a gateway on the directory"""
	def __init__(self, name):
		super(Gateway, self).__init__()
		self.name = name
		self.user = directory.User(name)
		self.user.addChild(directory.Gateways())
		self.gateway = directory.Gateway(name)
		self.user[-1].addChild(self.gateway)
		self.params = directory.Params()
		self.variables = directory.Variables()
		self.gateway.addChild(self.params)
		self.gateway.addChild(self.variables)

	def addParam(self, key, value):
		self.params.addChild(directory.Param(key, value))

	def addVariable(self, key, value):
		self.variables.addChild(directory.Variable(key, value))
		

class Directory(object):
	"""Represents a directory entry"""
	def __init__(self, domain):
		super(Directory, self).__init__()
		self.directory = directory.Directory()
		self.domain = self.directory.setDomain(domain)
		self.users = directory.Users()
		self.domain.addChild(self.users)
		self.gateways = []

	def serialize(self):
		return self.directory.serialize()

	def addGateway(self, name):
		proxyGateway = Gateway(name)
		self.users.addChild(proxyGateway.user)
		return proxyGateway

	def addUser(self, name):
		userProxy = User(name)
		self.users.addChild(userProxy.user)
		return userProxy
		
	def __repr__(self):
		return str(self.directory)

def notfound():
	section = Section(name='result')
	section.addChild(Result())
	return Document(section)