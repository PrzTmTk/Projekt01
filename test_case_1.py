from main import ptest01

def inc(x):
    return x + 1

def test_answer_1():
    assert inc(3) == 5

def test_answer_2():
    assert ptest01() == "test"

def test_answer_3():
    assert inc(3) == 4