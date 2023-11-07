import pytest
import unittest
from second_part.src import div, raise_something, add, ForceToList, random_gen, get_info
from second_part.src import CacheDecorator



def test_generator():
    g = random_gen()
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'

@CacheDecorator()
def add(a, b):
    return a + b

def test_cache_decorator():
    # Test caching with integer arguments
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(2, 3) == 5  \
    # Test caching with string arguments
    assert add("Hello, ", "world!") == "Hello, world!"
    assert add("Hello, ", "there!") == "Hello, there!"
    # Test caching with mixed types (integer and string)
    assert add(2, "Hello") == "2Hello"
    # Test a case where caching might fail
    assert add(2, "2") == "22"  #\




def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4

