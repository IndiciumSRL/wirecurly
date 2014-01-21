# -*- coding: utf-8 -*-
import logging

import pytest
from lxml import etree

from utils import xml2d

from wirecurly.serialize import XMLFactory

@pytest.mark.parametrize("data,expected", [
    (
        {'tag': 'domain', 'children': [{'tag': 'params', 'children': []}, {'tag': 'variables', 'children': []}, {'tag': 'users', 'children': []}], 'attrs': {'name': 'wirephone.com.ar'}},
        '<domain name="wirephone.com.ar"><users></users><params></params><variables></variables></domain>'
    ),
    (
        {'tag': 'domain', 'children': [{'tag': 'params', 'children': [{'tag': 'param', 'attrs': {'name': 'test', 'data': True} ,'children': []}]}, {'tag': 'variables', 'children': []}, {'tag': 'users', 'children': []}], 'attrs': {'name': u'wirephone.com.ar'}},
        '<domain name="wirephone.com.ar"><users></users><params><param name="test" data="true"/></params><variables></variables></domain>'
    )
])
def test_xml_factory(data, expected):
    f = XMLFactory(data)
    response = f.getXML()

    try:
        root = etree.fromstring(response)
        expected_root = etree.fromstring(expected)
    except:
        logging.exception('Invalid XML..')
        pytest.fail("Invalid XML: %s" % response)

    assert xml2d(root) == xml2d(expected_root)


def test_dict_typecasting():
    '''
        Test that we are able to typecast all dict keys and values to string
    '''
    d = {
        'int': 2,
        'bool_true': True,
        'bool_false': False,
        'float': 0.59,
        'unicode': u'João Mesquita'
    }

    f = XMLFactory({})
    new_d = f._typecastAttributes(d)
    for key, val in new_d.iteritems():
        assert (type(key) == str or type(key) == unicode)
        assert (type(val) == str or type(val) == unicode)