import logging
from wirecurly.exc import *
from wirecurly.dialplan.expression import *

log = logging.getLogger(__name__)

__all__ = ['Condition','or_']

class Condition(object):
    '''
        Condition oject for dialplan. expr must be a dictionary
    '''

    def __init__(self,attr=None,val=None,cont=False,expr=None):
        super(Condition, self).__init__()
        if not attr and not val:
            if not expr:
                expr = ExpressionAbs()
        else:
            expr = ExpressionField(attr,val)
        self.cont = cont
        self.attrs = expr.todict()
        self.actions = []
        self.antiactions = []

    def addAction(self,act,val,inline=False):
            '''
                Set a new action for this condition
            '''
            if self.existAction(act,val):   
                log.warning('Replacing existing action!')
            self.actions.append({'application' : act , 'data' : val, 'inline' : inline})

    def addAntiAction(self,act,val,inline=False):
            '''
                Set a new anti-action for this condition
            '''
            if self.existAntiAction(act,val):
                log.warning('Replacing existing anti-action!')

            self.antiactions.append({'application' : act , 'data' : val, 'inline' : inline})
            return

    def addApplication(self, app,inline=False):
        '''
            Add an application.
            An application must have 2 attributes. app_name and data.
        '''
        if not hasattr(app, 'app_name') or not hasattr(app, 'data'):
            raise NoSuchApplication
        else:
            self.addAction(app.app_name, app.data, inline)

    def existAction(self,act,val,inline=False):
            '''
                Return true if an action and data exists 
            '''
            for a in self.actions:
                if a.get('application') == act and a.get('data') == val and a.get('inline') == inline:
                    return True
            return False

    def existAntiAction(self,act,val,inline=False):
            '''
                Return true if an antiaction and data exists 
            '''
            for a in self.antiactions:
                if a.get('application') == act and a.get('data') == val and a.get('inline') == inline:
                    return True
            return False

    def todict(self):
        '''
            Create a dict so it can be converted/serialized
        '''
        children = []

        if self.actions:
            children.extend([{'tag': 'action', 'attrs': a} for a in self.actions])

        if self.antiactions:
            children.extend([{'tag': 'anti-action', 'attrs': a} for a in self.antiactions])

        if self.cont:
            self.attrs.update({'break': self.cont})
            
        return {'tag': 'condition', 'children': children, 'attrs': self.attrs }

class or_(object):
    '''
        Class to add conditions to an extensions to be evaluated with logical OR. 
        Can receive conditions or a list of conditions as parameters
    '''

    def __init__(self,*args):
        super(or_, self).__init__()
        self.conditions = []
        if type(args[0]) == list:
            for i in args[0]:
                self.conditions.append(i) 
        else:
            for i in args:
                self.conditions.append(i)


    def todict(self):
        '''
            Create a dict for dialplan to evaluate condition with logical or
        '''
        for i,cond in enumerate(self.conditions):
            if i < len(self.conditions)-1 and cond.attrs:
                self.conditions[i].attrs.update({'break':'on-true'})
        return self.conditions

