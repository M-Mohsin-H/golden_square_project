from lib.gratitudes import *
from lib.gratitudes import Gratitudes

def test_gratitudes():
    gratitude = Gratitudes()
    assert gratitude.format() == 'Be grateful for: '

def test_gratitudes1():
    gratitude = Gratitudes()
    gratitude.add("Health")
    assert gratitude.format() == "Be grateful for: Health" 

def test_gratitudes2():
    gratitude = Gratitudes()
    gratitude.add("Health")
    gratitude.add("Security")
    assert gratitude.format() == "Be grateful for: Health, Security" 

def test_gratitudes3():
    gratitude = Gratitudes()
    gratitude.add("Health")
    gratitude.add("Security")
    gratitude.add("Family")
    assert gratitude.format() == "Be grateful for: Health, Security, Family"