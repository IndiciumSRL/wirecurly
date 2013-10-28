from wirecurly.dialplan.applications import ApplicationBase

class Conference(ApplicationBase):
	"""The conference application"""
	def __init__(self, conf_name, profile='default'):
		super(Conference, self).__init__('conference')
		self.conf_name = conf_name
		self.profile = profile
		self.pin = None

	@property
	def data(self):
		'''
			Getter for data so we can properly manipulate application configuration
		'''
		if self.pin is None:
			return '{}@{}'.format(self.conf_name, self.profile)
		else:
			return '{}@{}+{}'.format(self.conf_name, self.profile, self.pin)

	def setPin(self, pin):
		'''
			Set conference PIN
		'''
		self.pin = pin

	def clearPin(self):
		'''
			Clear conference PIN
		'''
		self.pin = None