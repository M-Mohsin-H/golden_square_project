from lib.greet import *

# def test_greet():
#    result = greet(hazel)

# assert result == Hello, hazel!

def test_greet():
    result = greet("Hazel")

    assert result == "Hello, Hazel!"

