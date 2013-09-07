from wirecurly.base import Element

class Document(Element):
	"""A document to be served as a configuration"""
	def __init__(self, section):
		super(Document, self).__init__('document', type="freeswitch/xml")
		self.addChild(section)

class Section(Element):
	"""A document to be served as a configuration"""
	def __init__(self, name):
		super(Section, self).__init__('section', name=name)