import logging
from wirecurly.exc import *
from wirecurly.dialplan.expression import *
import os

log = logging.getLogger(__name__)

__all__ = ['FileString']

class FileString(object):
	'''
		Filestring oject to use with playback app in dialplan.
	'''

	def __init__(self,*argv):
		super(FileString, self).__init__()
		self.audios = []
		self.path = ''
		for i in argv:
			self.addAudio(i)


	def addAudio(self,audio):
		'''
			Add an audio file to FileString object
		'''
		self.audios.append(audio)

	def setPath(self,path):
		'''
			Set Path for audios
		'''
		self.path = path

	def toString(self):
		'''
			Return a string to use with playback app
		'''
		return 'file_string://%s' % '!'.join(['%s%s' % (self.path,a) for a in self.audios])

		