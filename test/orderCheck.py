import json

dict3='{"a":1,"b":3}'

dict1={"a":1,"b":2,"c":3}
dict2={"a":1,"d":6}

dict4=json.loads(dict3)
assert dict1["a"]+dict1["b"]==dict2["d"]
