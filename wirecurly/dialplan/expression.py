import logging

log = logging.getLogger(__name__)

__all__ = ['ExpressionBase','ExpressionAbs','ExpressionTime','ExpressionField']

class ExpressionBase(object):
	'''
		Base Class for expressions
	'''

	def __init__(self):
		super(ExpressionBase,self).__init__()

	def todict(self):
		'''
			to_dict must return a dict with all attributes
		'''
		raise NotImplementedError

class ExpressionAbs(ExpressionBase):
	'''
		Class for absolute expression
	'''

	def __init__(self):
		super(ExpressionAbs,self).__init__()

	def todict(self):
		'''
			Absolute expressions have no attributes
		'''
		return {}

class ExpressionTime(ExpressionBase):
	'''
		Class for Time expressions
	'''

	def __init__(self,wday,hour):
		super(ExpressionTime,self).__init__()
		self.wday = wday
		self.hour = hour

	def getWday(self):
		'''
			Return wday
		'''
		return self.wday
		
	def getHour(self):
		'''
			Return hour 
		'''
		return self.hour

	def setWday(self,wday):
		'''
			Set wday value
		'''
		self.wday = wday


	def setHour(self,wday):
		'''
			Set hour value
		'''
		self.hour = hour

	def todict(self):
		'''
			Return a dict with wday and hour
		'''
		return {'wday' : self.wday , 'hour' : self.hour}

class ExpressionField(ExpressionBase):
	'''
		Field expressions Class
	'''

	def __init__(self,field,exp):
		super(ExpressionField,self).__init__()
		self.field = field
		self.exp = exp

	def getField(self):
		'''
			Return field value
		'''
		return self.field
		
	def getExp(self):
		'''
			Return expression value 
		'''
		return self.exp

	def setField(self,field):
		'''
			Set field value
		'''
		self.field = field


	def setExp(self,exp):
		'''
			Set expression value
		'''
		self.hour = hour

	def todict(self):
		'''
			Return a dict with field and expression
		'''
		return {'field' : self.field , 'expression' : self.exp}

	