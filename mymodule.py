import json

with open('181.json', 'r+') as f:
    catalog = json.load(f)
    for i in range(3):
        name = input('Name of product: ')
        count = int(input('Count: '))
        if name not in catalog:
         catalog[name] = count
        else:
         catalog[name] += count
    x = json.dumps(catalog)

f.write(x)

