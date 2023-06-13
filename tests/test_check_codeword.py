from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword1():
    result = check_codeword("horsey")
    assert result == "WRONG!"

def test_check_codeword3():
    result = check_codeword("home")
    assert result == "Close, but nope."

    # def check_codeword(codeword):
    # if codeword == "horse":
    #     return "Correct! Come in."
    # elif codeword[0] == "h" and codeword[-1] == "e":
    #     return "Close, but nope."
    # else:
    #     return "WRONG!"