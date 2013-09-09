from wirecurly.base.dialplan import ApplicationBase

class Answer(ApplicationBase):
	"""Execute the answer of a call"""
	name = 'answer'
	def __init__(self):
		super(Answer, self).__init__()

class Hangup(ApplicationBase):
	"""Hangup a call"""
	name = 'hangup'
	def __init__(self, cause=None):
		super(Hangup, self).__init__()
		self.mdata = cause
		