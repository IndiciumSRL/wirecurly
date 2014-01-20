import logging

log = logging.getLogger(__name__)

__all__ = ['Domain']
        
class Domain(object):
    """A domain object for the directory"""
    def __init__(self, name):
        super(Domain, self).__init__()
        self.domain = name
        self.variables = []
        self.parameters = []
        self.users = []

    def addVariable(self, var, val):
        '''
            Set an extra variable for a domain
        '''
        try:
            self.getVariable(var)
        except ValueError:
            self.variables.append({'name': var, 'value': val})
            return

        log.warning('Cannot replace existing variable.')
        raise ValueError


    def addUser(self, user):
        '''Add user to domain
        
        :param user: The user to add to the domain.
        :type user: object
        '''
        self.users.append(user)

    def addParameter(self, param, val):
        '''
            Set an extra parameter for a domain
        '''
        try:
            self.getParameter(param)
        except ValueError:
            self.parameters.append({'name': param, 'value': val})
            return
        
        log.warning('Cannot replace existing parameter.')
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
        children.append({'tag': 'variables', 'children': [
                        {'tag': 'variable', 'attrs': v} for v in self.variables
                    ]})
        children.append({'tag': 'users', 'children': [
                        u.todict() for u in self.users
                    ]})
        return {'tag': 'domain', 'children': children, 'attrs': {'name': self.domain}}