from dialplan import *
from dialplan.applications import *


def main():
	c = Context('default')
	e = c.addExtension('test')
	cond = e.addCondition()

	cond.addAction( Answer() )
	cond.addAction( Hangup() )

	print c

if __name__ == '__main__':
	main()