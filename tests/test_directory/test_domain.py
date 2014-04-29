'''
    Creates all tests to serialize XMLs to xml_curl
'''
import logging

import pytest
from lxml import etree
from mock import Mock

from wirecurly.directory import Domain, User
   
def test_domain_no_users():
    domain = Domain('wirephone.com.ar')
    response = domain.todict()
    assert domain.domain == 'wirephone.com.ar'
    assert len(response['children']) == 0
    assert not domain.users

def test_domain_1_user():
    domain = Domain('wirephone.com.ar')
    user = Mock(User)
    domain.addUser(user)
    
    assert domain.users
    assert len(domain.users) == 1
    assert domain.users[0] == user
    response = domain.todict()
    assert len(response['children']) == 1
    assert response.get('children')[0] == user.todict()
