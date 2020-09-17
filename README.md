# python-gattr

allows access to nested objects
```
o = {'k1': {'n1k1': 'n1v1', n2k2: [10, 11, 12]}}
gattr(o, 'k1', 'n2k2', 2) # 12

gattr(o, 'k1', 'n2k2', 10, default='thedefault') # thedefault

gattr(o, 'k1', 'n2k2', 2, callback=lambda x: str(x)) # '12'
```
