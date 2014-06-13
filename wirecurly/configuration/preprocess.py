'''
    This module provides proprietary pre processing directives for FreeSWITCH configuration.
    It is mostly used for static configuration.
'''

import logging

log = logging.getLogger(__name__)


class PreprocessSet(object):
    """Set a global variable using a preprocess directive."""
    def __init__(self, variable, value):
        super(PreprocessSet, self).__init__()
        self.variable = variable
        self.value = value

    def todict(self):
        '''Create a dict so it can be converted/serialized

        :rtype: dict -- a dict ready to be serialized
        '''       
        return {'tag': 'X-PRE-PROCESS', 'children': [], 'attrs': {'cmd': 'set', 'data': '%s=%s' % (self.variable, self.value)}}
