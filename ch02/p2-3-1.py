import pprint as pp
import json
filename = 'jdata.json'
with open(filename, "rt") as fp:
    data = json.loads(fp.read())
pp.pprint(data)
    
