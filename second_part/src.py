
def random_gen():
    while True:  
        num = random.randint(10, 20)  
        yield num  
        if num == 15:  
            break  

generator = random_gen()  
for num in generator:  
    print(num)


def decorator_to_str(func):
    # todo exercise 2
     def inner(*args):
            result = func(args)
        result = str(result)
        return result

    return func


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']


def ignore_exception(exception):
    # todo exercise 3
    return lambda x: x
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return None

        return wrapper

    return decorator

@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList(type):
    # todo exercise 5
    def __new__(cls, name, bases, attrs):
        bases = (list,)
        return super().__new__(cls, name, bases, attrs)
    pass


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 4
    pass

class ProcessCheckMeta(type):
    def __init__(cls, name, bases, attrs):
        super(ProcessCheckMeta, cls).__init__(name, bases, attrs)

        if 'process' in attrs and callable(attrs['process']):
            process_func = attrs['process']
            if len(inspect.signature(process_func).parameters) != 3:
                raise ValueError(f"Class {name} has a 'process' method, but it doesn't take exactly 3 arguments.")