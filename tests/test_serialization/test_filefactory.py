'''
	Creates all tests to serialize XMLs to files
'''
import unittest
import os

from lxml import etree

from wirecurly import XMLFileFactory

class TestFileSerialization(unittest.TestCase):
	"""Test file serialization"""
	
	def setUp(self):
		'''
			Fixture for the filename to be used and its data
		'''
		self.data = {'tag': 'parent', 'children': [{'tag': 'child1', 'attrs': {'attr2': 'str2'}, 'children': [{'tag': 'child2', 'attrs': {'attr3': 'str3'}, 'children': []}]}], 'attrs': {'attr': 'str'} }
		self.filename = '/tmp/test.xml'

		self.fac = XMLFileFactory(self.data, self.filename)
		self.fac.convert()

	def tearDown(self):
		'''
			Remove generated files on tests
		'''
		try:
			os.unlink(self.filename)
		except OSError:
			# File does not exist, so we're fine
			pass

	def test_generated_file(self):
		'''
			Test that random data is generated and file is created.
		'''
		assert os.path.isfile(self.filename)

	def test_generated_file_content(self):
		'''
			Test that the file content is valid XML
		'''
		with open(self.filename, 'r') as f:
			etree.fromstring(f.read())

		assert True

	def test_generated_xml(self):
		'''
			Test the proper generation of XML
		'''
		etree.fromstring(self.fac.getXML())
		assert True
