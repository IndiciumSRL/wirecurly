from wirecurly.dialplan.applications import ApplicationBase

class Answer(ApplicationBase):
	"""The answer application"""
	def __init__(self):
		super(Answer, self).__init__('answer')

	@property
	def data(self):
		'''
			Answer does not need data, so return empty string.
		'''
		return ''

class Sleep(ApplicationBase):
	"""The sleep application"""
	def __init__(self, time_in_ms):
		super(Sleep, self).__init__('sleep')
		self.time_in_ms = time_in_ms
		
	@property
	def data(self):
		'''
			Sleep only needs to return the time to sleep in ms.
		'''
		return '%s' % self.time_in_ms

class Set(ApplicationBase):
	"""Set a variable on the current executing channel"""
	def __init__(self, variable, value):
		super(Set, self).__init__('set')
		self.variable = variable
		self.value = value

	@property
	def data(self):
		'''
			Set needs return a string
		'''
		return '%s=%s' % (self.variable, self.value)
		
class Export(ApplicationBase):
	"""Export a variable on the other b leg"""
	def __init__(self, variable, value, nolocal=False):
		super(Export, self).__init__('export')
		self.variable = variable
		self.value = value
		self.nolocal = nolocal

	@property
	def data(self):
		'''
			Set needs return a string
		'''
		if self.nolocal:
			return 'nolocal:%s=%s' % (self.variable, self.value)
		else:
			return '%s=%s' % (self.variable, self.value)