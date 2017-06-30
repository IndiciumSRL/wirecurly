'''
	Test generic list creation
'''

import unittest
from wirecurly.configuration.genericlist import GenericList
from wirecurly.configuration.elementlist import ElementList


class testGenericListCreation(unittest.TestCase):
    '''
        Test generic list creation
    '''

    def setUp(self):
        '''
        list fixtures for tests
        '''
        self.list = GenericList('test', {'first_attribute': 'test_attr'})

    def test_list_dict_ok(self):
        '''
            Test that list is properly serialized
        '''
        assert isinstance(self.list.todict(), dict)
        assert self.list.todict() == {'tag': 'test', 'attrs': {'first_attribute': 'test_attr'}, 'children': []}

    def test_adding_element(self):
        '''
            Test if an element is properly add to a list
        '''
        e = ElementList('name', {'type': 'some_type'})
        self.list.addElement(e)
        el = self.list.getElements()
        assert el[0].todict() == {'tag': 'name', 'attrs': {'type': 'some_type'}}
