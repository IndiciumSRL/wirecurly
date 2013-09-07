import logging

from wirecurly.base import Element
from wirecurly.base.configuration import Document, Section as SectionBase

log = logging.getLogger(__name__)

__all__ = ['notfound']
		
class Result(Element):
	"""The result to be used when something was not found"""
	def __init__(self):
		super(Result, self).__init__('result', status='not found')
		

def notfound():
	section = SectionBase(name='result')
	section.addChild(Result())
	return Document(section)