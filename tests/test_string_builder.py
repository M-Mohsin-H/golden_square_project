from lib.string_builder import * 

def test_StringBuilder():
    stringbuilder = StringBuilder()
    # assert stringbuilder.add == ""
    # assert stringbuilder.size == 0
    assert stringbuilder.output() == ""

def test_StringBuilder_add_1_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("a") 
    # assert stringbuilder.size() == 1
    assert stringbuilder.output() == "a"

def test_StringBuilder_checks_string_size():
    stringbuilder = StringBuilder()
    stringbuilder.add("a") 
    assert stringbuilder.size() == 1

def test_StringBuilder_adding_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("a") 
    stringbuilder.add(" ") 
    stringbuilder.add("beautiful") 
    stringbuilder.add(" ") 
    stringbuilder.add("day") 
    assert stringbuilder.output() == "a beautiful day"

def test_StringBuilder_check_size_for_adding_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("a") 
    stringbuilder.add(" ") 
    stringbuilder.add("beautiful") 
    stringbuilder.add(" ") 
    stringbuilder.add("day") 
    assert stringbuilder.size() == 15