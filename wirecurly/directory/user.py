import logging

log = logging.getLogger(__name__)

__all__ = ['User']
        
class User(object):
    """A user object for the directory"""
    def __init__(self, user_id, password=None):
        super(User, self).__init__()
        self.user_id = user_id
        self.variables = []
        self.parameters = []
        if password:
            self.addParameter('password', password)

    def addVariable(self, var, val):
        '''
            Set an extra variable for an user
        '''
        try:
            self.getVariable(var)
        except ValueError:
            self.variables.append({'name': var, 'value': val})
            return

        log.warning('Cannot replace existing variable.')
        raise ValueError


    def addParameter(self, param, val):
        '''
            Set an extra parameter for an user
        '''
        try:
            self.getParameter(param)
        except ValueError:
            self.parameters.append({'name': param, 'value': val})
            return
        
        log.warning('Cannot replace existing parameter. (%s) %s for %s', param, self.getParameter(param), val)
        raise ValueError

    def getParameter(self, param):
        '''
            Retrieve the value of a parameter by its name
        '''
        for p in self.parameters:
            if p.get('name') == param:
                return p.get('value')

        raise ValueError

    def getVariable(self, var):
        '''
            Retrieve the value of a variable by its name
        '''
        for v in self.variables:
            if v.get('name') == var:
                return v.get('value')

        raise ValueError


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        children = [{'tag': 'params', 'children': [
                        {'tag': 'param', 'attrs': p} for p in self.parameters
                    ]}]
        if self.variables:
            children.append({'tag': 'variables', 'children': [
                            {'tag': 'variable', 'attrs': v} for v in self.variables
                        ]})
        return {'tag': 'user', 'children': children, 'attrs': {'id': self.user_id}}