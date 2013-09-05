from dialplan import *
from dialplan.applications import *


def main():
	c = Context('default')
	e = Extension('test')
	c.addChild(e)
	cond = Condition()
	e.addChild(cond)
	cond.addChild( Action( Answer() ) )
	print c

if __name__ == '__main__':
	main()