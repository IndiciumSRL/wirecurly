import logging

log = logging.getLogger(__name__)


class Entry(object):
    """Set an entry."""
    def __init__(self, action, digits,param):
        super(Entry, self).__init__()
        self.action = action
        self.digits = digits
        self.param = param

    def todict(self):
        '''Create a dict so it can be converted/serialized'''
        return {'tag': 'entry', 'children': [], 'attrs': {'action' : self.action , 'digits' : self.digits , 'param' : self.param}}