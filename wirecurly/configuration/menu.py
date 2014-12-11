import logging

log = logging.getLogger(__name__)

__all__ = ['Menu']

class Menu(object):
	'''
		Menu object to build IVR
	'''
	def __init__(self,name):
		super(Menu, self).__init__()
		self.attributes = {'name': name}
		self.entries = []
		self.include = []
		

	def addAttr(self,attr,val):
		'''
			Add an attribute to menu object
		'''
		try:
			self.getAttr(attr)
		except ValueError:
			self.attributes[attr] = val
			return
		log.warning('Cannot modify existing attribute')
		raise ValueError

	def getAttr(self,attr):
		'''
			Get attribute from menu by its name. If it doesnt exist then raise an exception
		'''
		val = self.attributes.get(attr)
		if not val:
			raise ValueError
		else:
			return val
		
	def addEntry(self,action,digits,param):
		'''
			Add entry tag to menu
		'''
		try:
			self.getEntry(digits)
		except ValueError:
			self.entries.append({'action' : action , 'digits' : digits , 'param' : param})
			return
		log.warning('Cannot replace existing entry')
		raise ValueError


	def getEntry(self,digits):
		'''
			Get an entry from menu object by its digit attribute
		'''

		for e in self.entries:
			if e['digits'] == digits:
				return e
		raise ValueError

	def addInclude(self,value):
		'''
			Add include entry for menu
		'''
		self.include.append({'tag': 'X-PRE-PROCESS', 'children': [], 'attrs': {'cmd': 'include', 'data': '%s' % (value)}})	
	
	def todict(self):
		'''
			Create a dict so it can be converted/serialized
		'''
	
		children = []

		if self.entries:
			children.extend([{'tag': 'entry', 'attrs': a} for a in self.entries])
		
		return {'tag': 'menu', 'children': children, 'attrs': self.attributes }
