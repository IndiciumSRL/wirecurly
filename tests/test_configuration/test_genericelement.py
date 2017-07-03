'''
	Test element creation for generic lists
'''

import unittest
from wirecurly.configuration import genericelement, param


class testElementCreation(unittest.TestCase):
    '''
		Test element creation
    '''

    def setUp(self):
        '''
			element fixtures for tests
        '''

        self.element = genericelement.GenericElement('name', {'type': 'some_type'})

    def test_element_dict_ok(self):
        '''
			Test that element is properly serialized
        '''
        assert isinstance(self.element.todict(), dict)
        assert self.element.todict() == {'tag': 'name', 'attrs': {'type': 'some_type'}}

    def test_element_with_subelement(self):
        '''
            Test that element with subelement is properly serialized
        '''
        assert isinstance(self.element.todict(), dict)
        subelement = param.Param('param_name', 'param_value')
        self.element.addElement(subelement)
        assert self.element.todict() == {'tag': 'name', 'attrs': {'type': 'some_type'}, 'children': [{'attrs': {'name': 'param_name', 'value': 'param_value'}, 'children': [], 'tag': 'param'}]}