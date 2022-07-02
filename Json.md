import json

df = [
    {'a':1,'b':2,'c':3},
    {'a':4,'b':5,'c':6},
    {'a':7,'b':8,'c':9}
]

stringfile = ""
for line in df:
    stringfile = stringfile + json.dumps(line) + "\n"

with open("your_json_file.jsonl", "w") as fp:
    fp.write(stringfile)