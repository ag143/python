import json

json_data = '{"python": 1, "php": 2, "c": 3, "vb": 4, "perl": 5}'

json_load = (json.loads(json_data))

print(json.dumps(json_load, indent=4))
