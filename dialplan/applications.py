from dialplan import ApplicationBase

class Answer(ApplicationBase):
	"""Execute the answer of a call"""
	def __init__(self):
		super(Answer, self).__init__()

	def application(self):
		return 'answer'