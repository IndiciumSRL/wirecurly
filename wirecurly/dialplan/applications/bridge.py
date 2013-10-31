from wirecurly.dialplan.applications import ApplicationBase

class Bridge(ApplicationBase):
	"""Bridge application"""
	def __init__(self, dialstring):
		super(Bridge, self).__init__('bridge')
		self.dialstring = dialstring

	@property
	def data(self):
		'''
			Data is the whole dialstring
		'''
		return self.dialstring