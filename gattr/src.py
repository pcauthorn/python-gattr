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
