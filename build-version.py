import os

fversion = 'stdeb.cfg'
f=open(fversion,"r")
lines=[]
for line in f:
    if "Debian-Version" in line:
        data=line.split(' ')
        newline = "Debian-Version: %s" % os.getenv('TRAVIS_BUILD_NUMBER')
        lines.append(newline)
    else:
        lines.append(line)
f.close

g=open(fversion, "w+")
for l in lines:
    g.write(l)
g.close
