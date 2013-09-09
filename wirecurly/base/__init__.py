from lxml import etree

class Element(object):
	"""Represents an element on the XML tree"""
	def __init__(self, tag, **attrs):
		super(Element, self).__init__()
		self.tag = tag
		self.__children = []
		self.__attrs = attrs
		self.__current_child = None
		self.__obj = None

	def addChild(self, child):
		self.__children.append(child)
		self.__current_child = child

	def __serializeAttrs(self):
		'''
			Serialize/sanitize attributes so that they get properly casted to its string equivalents
		'''
		sattrs = {}
		for k,v in self.__attrs.iteritems():
			if v is None:
				sattrs[k] = ''
			elif isinstance(v, bool):
				if v: sattrs[k] = 'true'
				else: sattrs[k] = 'false'
			else:
				sattrs[k] = v
		return sattrs


	def tree(self):
		'''
			Create a XML structure based on this element
		'''
		obj = etree.Element(self.tag, self.__serializeAttrs() )
		for c in self.__children:
			obj.append(c.tree())
		return obj

	def serialize(self):
		'''
			Serialize the tree
		'''
		return etree.tostring(self.tree(), pretty_print=False)

	def __getitem__(self, key):
		return self.__children[key]

	def __setitem__(self, key, value):
		self.__children[key] = value

	def __repr__(self):
		'''
			Pretty print our XML
		'''
		return etree.tostring(self.tree(), pretty_print=True)
