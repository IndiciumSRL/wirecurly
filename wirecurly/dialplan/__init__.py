import logging
from uuid import uuid4

from wirecurly.base import dialplan

log = logging.getLogger(__name__)

class Dialplan(object):
	"""High level dialplan object"""
	def __init__(self, context):
		super(Dialplan, self).__init__()
		self.context = dialplan.Context(context)

	def addExtension(self, name):
		'''
			Add a new extension to the current context
		'''
		exten = dialplan.Extension(name)
		self.context.addChild(exten)
		return self.context[-1]

	def addCondition(self, *args, **kwargs):
		'''
			Add a new condition with a new extension
		'''
		exten = dialplan.Extension(str(uuid4()))
		cond = dialplan.Condition(*args, **kwargs)
		exten.addChild(cond)
		self.context.addChild(exten)
		return cond


	def serialize(self):
		return self.context.serialize()

	def __repr__(self):
		return self.context.__repr__()