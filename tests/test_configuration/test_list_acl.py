'''
	Test list creation
'''

import unittest
from wirecurly.configuration import list, node


class testListCreation(unittest.TestCase):
    '''
        Test menu creation
    '''

    def setUp(self):
        '''
        list fixtures for tests
        '''
        self.list = list.List('gateways','deny')

    def test_list_dict_ok(self):
        '''
            Test that list is properly serialized
        '''
        assert isinstance(self.list.todict(), dict)

    def test_adding_node(self):
        '''
            Test if a node is properly add to a list
        '''
        n = node.Node('allow', '10.10.10.10/32')
        self.list.addNode(n)
        nl = self.list.getNodes()
        assert nl[0].todict() == {'tag': 'node', 'attrs': {'cidr': '10.10.10.10/32', 'type': 'allow'}}
