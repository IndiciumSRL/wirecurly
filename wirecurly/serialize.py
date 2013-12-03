'''
	This module will provide XML serialization methods
'''
import sys
import logging

try:
	from lxml import etree
except ImportError:
	log.exception('lxml is needed for wirecurly to be used.')
	sys.exit(1)

__all__ = ['XMLFileFactory']

log = logging.getLogger(__name__)

class XMLFactory(object):
	"""Base factory for XML generation"""
	def __init__(self, data):
		super(XMLFactory, self).__init__()
		self.data = data
		
	def getXML(self):
		'''
			Get the XML based on the data provided.
		'''
		self.root = etree.Element(self.data.get('tag'), **self.data.get('attrs', {}))
		if self.data.get('children'):
			self._parseChildren(self.data.get('children'), self.root)

		return etree.tostring(self.root, pretty_print=True)

	def _parseChildren(self, children, parent):
		'''
			Parse children of the dict to create XML structure
		'''
		for child in children:
			el = etree.SubElement(parent, child.get('tag'), **child.get('attrs', {}))
			if child.get('children'):
				self._parseChildren(child.get('children'), el)

	def convert(self):
		'''
			Abstract method that will serialize the XML as per the factory specification
		'''
		raise NotImplementedError

class XMLFileFactory(XMLFactory):
	'''Object that will serialize XML to a specific file.

	:param data: The object to serialize.
	:type data: object
	:param filepath: The absolute file path and name to serialize to.
	:type filepath: str
	:param include: If the include parameter is True, then an <include/> tag will be the parent node of the structure to serialize.
	:type include: bool
	'''
	def __init__(self, data, filepath, include=False):
		if include:
			data = {'tag': 'include', 'children': [data]}
		super(XMLFileFactory, self).__init__(data)
		self.filepath = filepath

	def convert(self):
		'''Generate XML and save it to filepath

		:raises: OSError
		'''
		with open(self.filepath, 'w') as f:
			f.write(self.getXML())
		