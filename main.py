import xmltodict
import json
import sys

var = sys.argv[1]
xmldocument = var
obj = xmltodict.parse(xmldocument)
result = json.dumps(obj)
print(result)