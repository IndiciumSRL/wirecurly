import logging

from base import Element

log = logging.getLogger(__name__)

__all__ = ['Context', 'Extension', 'Condition', 'Action', 'ApplicationBase']

class Context(Element):
	"""A dialplan context"""
	def __init__(self, name):
		super(Context, self).__init__('context', name=name)


class Extension(Element):
	"""Represents a dialplan extension"""
	def __init__(self, name, _continue=False):
		d = {}
		if _continue:
			d['continue'] = _continue
		super(Extension, self).__init__('extension', name=name, **d)
		
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
		
class Action(Element):
	"""Represents an action"""
	def __init__(self, application, negate=False):
		if not isinstance(application, ApplicationBase):
			raise Exception('Application needs to inherit ApplicationBase')

		d = {'application': application.application(), 'data': application.data()}
		if negate:
			super(Action, self).__init__('anti-action', **d)
		else:
			super(Action, self).__init__('action', **d)
		
class ApplicationBase(object):
	"""An abstract base for an application"""
	def __init__(self):
		super(ApplicationBase, self).__init__()
	
	def application(self):
		raise NotImplementedError
		
	def data(self):
		return None