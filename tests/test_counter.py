from lib.counter import *

def test_counter():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter1():
    counter = Counter()
    counter.add(1)
    assert counter.report() == "Counted to 1 so far."

def test_counter2():
    counter = Counter()
    counter.add(5)
    counter.add(4)
    counter.add(1)
    assert counter.report() == "Counted to 10 so far."

# def test_counter():
#     counter = Counter()
#     counter.add()
#     result = counter.report()
#     assert == "Counted to 0 so far."