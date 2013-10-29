from wirecurly.dialplan.applications import ApplicationBase

class Playback(ApplicationBase):
	"""The playback application"""
	def __init__(self, filename):
		super(Playback, self).__init__('playback')
		self.filename = filename

	@property
	def data(self):
		'''
			Filename only returns the file to be played.
			We cannot make checks of file existence unless we are on the local machine.
		'''
		return self.filename