'''
	Test element creation for generic lists
'''

import unittest
from wirecurly.configuration import elementList


class testElementCreation(unittest.TestCase):
    '''
		Test element creation
    '''

    def setUp(self):
        '''
			element fixtures for tests
        '''

        self.element = elementList.elementList({'element_name': 'name', 'type': 'some_type'})

    def test_element_dict_ok(self):
        '''
			Test that element is properly serialized
        '''
        assert isinstance(self.element.todict(), dict)
        assert self.element.todict() == {'tag': 'name', 'attrs': {'type': 'some_type'}}