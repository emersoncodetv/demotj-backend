import sys
import json

hola = sys.argv[1]

print(json.dumps(dict({"a": 1, "b": 2})))
