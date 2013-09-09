import logging

from wirecurly.base import Element

log = logging.getLogger(__name__)

__all__ = ['Context', 'Extension', 'Condition', 'Action', 'ApplicationBase']

class Context(Element):
	"""A dialplan context"""
	def __init__(self, name):
		super(Context, self).__init__('context', name=name)

	def addExtension(self, name, *args, **kwargs):
		e = Extension(name, *args, **kwargs)
		self.addChild(e)
		return e


class Extension(Element):
	"""Represents a dialplan extension"""
	def __init__(self, name, _continue=False):
		d = {}
		if _continue:
			d['continue'] = _continue
		super(Extension, self).__init__('extension', name=name, **d)

	def addCondition(self, *args, **kwargs):
		cond = Condition(*args, **kwargs)
		self.addChild(cond)
		return cond
		
class Condition(Element):
	"""Represents a condition"""
	def __init__(self, field=None, expression=None, _break=None):
		d = {}
		if field is not None:
			if expression is not None:
				d = {'expression': expression, 'field': field}
		if _break is not None:
			if _break not in ('on-true', 'on-false', 'never'):
				log.warning('Invalid break value (%s), ignoring.', _break)
			else:
				d['break'] = _break

		super(Condition, self).__init__('condition', **d)

	def addAction(self, application, negate=False):
		action = Action(application, negate)
		self.addChild( action )
		return action
		
class Action(Element):
	"""Represents an action"""
	def __init__(self, application, negate=False):
		if not isinstance(application, ApplicationBase):
			raise Exception('Application needs to inherit ApplicationBase')

		d = {'application': application.application()}
		data = application.data()
		if data is not None:
			d['data'] = data
		if negate:
			super(Action, self).__init__('anti-action', **d)
		else:
			super(Action, self).__init__('action', **d)
		
class ApplicationBase(object):
	"""An abstract base for an application"""
	name = None
	mdata = None
	def __init__(self):
		super(ApplicationBase, self).__init__()
	
	def application(self):
		if self.name is None:
			raise NotImplementedError
		return self.name
		
	def data(self):
		if hasattr(self.mdata, '__call__'):
			return self.mdata()
		else:
			return self.mdata
