

import json
import os
uns=[]
with open('dep.json') as f:
	data = json.load(f)
for key in data:
	x="pip3 install "+ str(key)+"=="+str(data[key])
	os.system(x + "> temp")
	out=open('temp', 'r').readlines()
	x=[i.split(' ')for i in out]
	if x[-1][0]=='Successfully':
		pass
	else:
		uns.append(key)
if len(uns)==0:
	print("All packages are Successfully Installed")
else:
	print("The list of packages not Successfully Installed are")
	print(uns)