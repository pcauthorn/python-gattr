def gattr(obj, *args, callback=None, default=None, invoke_callables=False):
    cb = callback or (lambda x: x)
    try:
        for arg in args:
            if hasattr(obj, '__getitem__'):
                obj = obj[arg]
            else:
                obj = getattr(obj, arg)
                if invoke_callables and callable(obj):
                    obj = obj()
            if obj is None:
                return default
        return cb(obj)
    except (AttributeError, IndexError, KeyError, TypeError):
        return default


if __name__ == '__main__':
    o = {'k1': {'n1k1': 'n1v1', 'n2k2': [10, 11, 12]}}
    print(gattr(o, 'k1', 'n2k2', 2))
