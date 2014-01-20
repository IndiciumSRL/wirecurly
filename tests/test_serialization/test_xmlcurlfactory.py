'''
    Creates all tests to serialize XMLs to xml_curl
'''
import logging
import StringIO
import pytest
from lxml import etree

from wirecurly import XMLCurlFactory
   
def test_not_found():
    '''
        Test generation of not found
    '''
    f = XMLCurlFactory()
    response = f.convert()
  
    # parse xml
    try:
        root = etree.fromstring(response)
    except:
        logging.exception('Invalid XML..')
        pytest.fail("Invalid XML: %s" % response)
        
    # without XSD validation, we can validate tags manually
    assert(root.tag == "document", "Invalid XML root")
    assert(root.attrib.has_key("type"), "Missing root attrib 'type'")
    assert(root.attrib["type"] == "freeswitch/xml", "Invalid value for root attrib 'type'")
    
    # validate section
    section = root.findall("section") 
    assert(len(section) == 1, "Has to be exactly one section")
    assert(section[0].attrib.has_key("name"), "Missing section attrib 'name'")
    assert(section[0].attrib["name"] == "result", "Invalid value for section attrib 'name'")
    
    # validate result
    result = section[0].findall("result")
    assert(len(result) == 1, "Has to be exactly one result")
    assert(result[0].attrib.has_key("status"), "Missing result attrib 'status'")
    assert(result[0].attrib["status"] == "not found", "Result status must be 'not found'")

@pytest.mark.parametrize("data,section,expected", [
    ({'tag': 'domain', 'children': [{'tag': 'params', 'children': []}, {'tag': 'variables', 'children': []}, {'tag': 'users', 'children': []}], 'attrs': {'name': 'wirephone.com.ar'}}, 'directory', '<document type="freeswitch/xml"><section name="directory"><domain name="wirephone.com.ar"><users></users><params></params><variables></variables></domain></section></document>')
])
def test_curl_serialization(data, section, expected):
    '''
    ''' 
    f = XMLCurlFactory(data, section)
    response = f.convert()
    try:
        root = etree.fromstring(response)
        expected_root = etree.fromstring(expected)
    except:
        logging.exception('Invalid XML..')
        pytest.fail("Invalid XML: %s" % response)
    
    def recursive_dict(element):
        return element.tag, \
            dict(map(recursive_dict, element)) or element.text

    d = recursive_dict(root)
    d2 = recursive_dict(expected_root)
    diff = set(d[1].keys()) - set(d2[1].keys())
    assert d[0] == d2[0]
    assert not diff