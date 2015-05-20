import logging

log = logging.getLogger(__name__)

class Configuration(object):
    '''
        A configuration object
    '''

    def __init__(self,name, description=None):
        super(Configuration, self).__init__()
        self.name = name
        self.description = description
        self.parameters = []

    def addParameter(self, param, val):
        '''
            Set an extra parameter for a Configuration object
        '''
        if not self.parameters:
            self.parameters = []
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
        if self.parameters:
            for p in self.parameters:
                if p.get('name') == param:
                    return p.get('value')

        raise ValueError


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        children = []
        if self.parameters:
            children.append({'tag': 'params', 'children': [
                            {'tag': 'param', 'attrs': p} for p in self.parameters
                        ]})
        if self.description:
            return {'tag': 'configuration', 'children': children, 'attrs': {'name': self.name, 'description': self.description }}
        else:
            return {'tag': 'configuration', 'children': children, 'attrs': {'name': self.name}}



class Section(object):
    """A section of a configuration object"""
    def __init__(self, name):
        super(Section, self).__init__()
        self.name = name
        self.variables = []
        

    def addVariable(self, variable):
        '''
        '''
        self.variables.append(variable)

    def todict(self):
        '''
        '''
        children = []
        #children.append(v.todict() for v in self.variables)
        children = [v.todict() for v in self.variables]
        
        return {'tag': self.name, 'children': children}
