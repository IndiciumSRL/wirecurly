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
		return self.time_in_ms