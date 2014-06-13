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

__all__ = ['XMLFileFactory', 'XMLFileFactory', 'XMLCurlFactory']

log = logging.getLogger(__name__)


class XMLFactory(object):
	"""Base factory for XML generation

	:param data: A dict with the specified format for XML generation
	:type data: dict
	"""
	def __init__(self, data):
		super(XMLFactory, self).__init__()
		self.data = data
		
	
	def _typecastAttributes(self, d):
		''' Typecast attributes to string or unicode

		:param d: the attributes dictionary
		:type d: dict

		:rtype: dict -- The new dict with only strings and unicodes
		'''
		for key in d:
			val = d[key]
			if type(val) == bool:
				if val == True:
					d[key] = 'true'
				else:
					d[key] = 'false'
			elif type(val) == int:
				d[key] = str(val)
			elif type(val) == float:
				d[key] = str(val)
			elif val is None:
				d[key] = u''
		return d

	def getXML(self):
		'''Get the XML based on the data provided.

		:rtype: str - A string generated XML for `data`
		'''
		self.root = etree.Element(self.data.get('tag'), **self._typecastAttributes(self.data.get('attrs', {})))
		if self.data.get('children'):
			self._parseChildren(self.data.get('children'), self.root)

		return etree.tostring(self.root, pretty_print=True)

	def _parseChildren(self, children, parent):
		'''
			Parse children of the dict to create XML structure
		'''
		for child in children:
			el = etree.SubElement(parent, child.get('tag'), **self._typecastAttributes(child.get('attrs', {})))
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
			if type(data) is list:
				data = {'tag': 'include', 'children': data}
			else:
				data = {'tag': 'include', 'children': [data]}
		super(XMLFileFactory, self).__init__(data)
		self.filepath = filepath

	def convert(self):
		'''Generate XML and save it to filepath

		:raises: OSError
		'''
		with open(self.filepath, 'w') as f:
			f.write(self.getXML())
		

class XMLCurlFactory(XMLFactory):
	'''Object that will serialize XML to mod_xml_curl

	:param data: The object to serialize.
	:type data: object
	:param section: The section to serialize.
	:type section: string
	'''
	def __init__(self, data=None, section=None):
		super(XMLCurlFactory, self).__init__(data)
		self.section = section

	def convert(self):
		'''Generate XML and serialize as per mod_xml_curl specification

		:rtype: a unicode string with a serialize XML
		'''
		if self.data is None:
			return self.not_found()
		self.getXML()
		document = etree.Element('document', type='freeswitch/xml')
		element = etree.SubElement(document, 'section', name=self.section)
		element.append(self.root)
		return etree.tostring(document, pretty_print=True, encoding='utf-8', xml_declaration=True)

	def not_found(self):
		'''Returns a not found XML as per mod_xml_curl specification'''
		root = etree.Element('document', type='freeswitch/xml')
		section = etree.SubElement(root, 'section', name='result')
		etree.SubElement(section, 'result', status='not found')
		return etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)