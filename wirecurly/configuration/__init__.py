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
        self.sections = []

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

    def addSection(self,section):
        '''
            Add a section object to configuration
        '''
        self.sections.append(section)


    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        children = []
        if self.parameters:
            children.append({'tag': 'params', 'children': [
                            {'tag': 'param', 'attrs': p} for p in self.parameters
                        ]})

        if self.sections:
            children = children + [s.todict() for s in self.sections]

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
            Add an object to Section. This obejct must contain a todict method.
        '''
        self.variables.append(variable)

    def todict(self):
        '''
            Convert Section to a dictionary
        '''
        children = []
        children = [v.todict() for v in self.variables]
        
        return {'tag': self.name, 'children': children}
