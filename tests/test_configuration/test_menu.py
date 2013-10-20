'''
	Test menu creation
'''

import unittest
from wirecurly.configuration import menu
from nose import tools


class testMenuCreation(unittest.TestCase):
	'''
		Test menu creation
	'''

	def setUp(self):
		'''
			menu fixtures for tests
		'''

		self.menu = menu.Menu('on_hours')
		
	def test_menu_dict_ok(self):
		'''
			Test that menu is properly serialized 
		'''
		assert isinstance(self.menu.todict(), dict)

	def test_adding_attr(self):
		'''
			Test if an attr is properly add to a menu
		'''
		self.menu.addAttr('digit-len','4') 
		assert self.menu.get('digit-len') == '4'

	@tools.raises(ValueError)
	def test_adding_existing_attr(self):
		'''
			Test adding an existing attr
		'''
		self.menu.addAttr('digit-len','4')
		self.menu.addAttr('digit-len','4')

	def test_adding_entry(self):
		'''
			Test if an entry is properly add to a menu
		'''
		self.menu.addEntry('menu-exec-app','1','transfer 1001 XML default') 
		assert self.menu.getEntry('menu-exec-app','1') == 'transfer 1001 XML default'

	@tools.raises(ValueError)
	def test_adding_existing_entry(self):
		'''
			Test adding an existing entry
		'''
		self.menu.addEntry('menu-exec-app','1','transfer 1001 XML default')
		self.menu.addEntry('menu-exec-app','1','transfer 1001 XML default')
		