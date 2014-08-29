import logging

log = logging.getLogger(__name__)


class Param(object):
    """Set a param."""
    def __init__(self, name, value):
        super(Param, self).__init__()
        self.name = name
        self.value = value

    def todict(self):
        '''Create a dict so it can be converted/serialized'''
        return {'tag': 'param', 'children': [], 'attrs': {'name': '%s' % self.name , 'value': '%s' % self.value}}
      